import os
from time import sleep
from typing import Optional, List, Dict
from pprint import pprint
import constants as const

ORDERINGS = ['Ascending', 'Descending']
CRITERIAS = ['Name', 'Surname', '', 'PhoneNumberCode']
SEPARATORS = {':', '-'}

VALIDATION_STRINGS = {
    "sep": "the separator should be `:` or `-`",
    "phone_len": "phone number must be at length 9",
    "phone_digit": "phone number should be digits only",
}
ORDERING_MAPPER = {
    "Ascending": False,
    "Descending": True
}

COLUMN_INDEX = 0
MAX_SURNAME_VAL = 0


def _make_file_path(file_path: str) -> str:
    curr_dir = os.getcwd()
    abs_path = os.path.join(curr_dir, file_path)
    return abs_path


def _file_handler(abs_path: str) -> Optional[List[str]]:
    content = None
    if not os.path.exists(abs_path):
        print(const.INPUT_FILE_WARNING)
    else:
        with open(abs_path, 'r') as rd:
            content = rd.readlines()
    return content


def _ask_validate_secondary_input(inp_msg: str, inp_options: List[str]) -> str:
    options_set = set(inp_options)
    sec_inp = input(inp_msg)
    flag = True
    while flag:
        if sec_inp not in options_set:
            sec_inp = input(f"The chosen option doesn't exist ! Valid options {inp_options}\n")
        else:
            flag = False
    return sec_inp


def _validate_separator(sep_placeholder: str) -> List[str]:
    warnings = []
    if sep_placeholder not in SEPARATORS:
        warnings.append('sep')
    return warnings


def _validate_phone_part(phone_placeholder: str) -> List[str]:
    warnings = []
    if len(phone_placeholder) != 9:
        warnings.append('phone_len')
    if not phone_placeholder.isdecimal():
        warnings.append('phone_digit')
    return warnings


def custom_sorting_method(element):
    key_value = element[COLUMN_INDEX]
    if COLUMN_INDEX == 3:
        try:
            return int(key_value[:3])
        except ValueError as ve:
            print(ve)
            return 0
    if key_value == '':
        ret_val = (MAX_SURNAME_VAL + 1) * 'Z'
    else:
        ret_val = key_value
    return ret_val


def _process_print_validations(validation_form: Dict):
    print("\nValidations")
    for line_num, line_warns in validation_form.items():
        valids_string = ', '.join(map(lambda x: VALIDATION_STRINGS.get(x), line_warns))
        valid_report_form = f"line {line_num}: {valids_string}"
        print(valid_report_form)


def _process_print_sorting(content_data: List[List[str]], criteria: str, ordering: str):
    global COLUMN_INDEX
    COLUMN_INDEX = CRITERIAS.index(criteria)
    ordered_content = sorted(content_data, key=custom_sorting_method, reverse=ORDERING_MAPPER[ordering])
    print("\nFile structure")
    pprint(list(map(lambda x: ' '.join(x), ordered_content)))


def _process_data_with_inputs(content_data: List[List[str]], criteria: str, ordering: str):
    validation_form = {}
    _validate_lines(content_data, validation_form)
    _process_print_sorting(content_data, criteria, ordering)
    _process_print_validations(validation_form)


def _validate_lines(content_data: List[List[str]], validation_form: Dict):
    global MAX_SURNAME_VAL
    for line_idx, line in enumerate(content_data):
        name, surname, separator, phone_num = line
        if len(surname) > MAX_SURNAME_VAL:
            MAX_SURNAME_VAL = len(surname)

        sep_res = _validate_separator(separator)
        phone_res = _validate_phone_part(phone_num)
        valid_sum = sep_res + phone_res
        if any(valid_sum):
            validation_form[line_idx + 1] = valid_sum


def _validate_content(content_lines: List[str]):
    if content_lines is None:
        print(const.EXIT_STR)
        sleep(2)
        exit()


def manage_process():
    file_path = input(const.first_msg)
    file_abspath = _make_file_path(file_path)
    content_lines = _file_handler(file_abspath)
    _validate_content(content_lines)

    ordering = _ask_validate_secondary_input(
        const.ORDER_INPUT_STR,
        ORDERINGS
    )
    criteria = _ask_validate_secondary_input(
        const.CRITERIA_INPUT_STR,
        CRITERIAS
    )
    content_data = list(
        map(
            lambda linex: linex.strip().split(' '),
            content_lines
        )
    )
    _process_data_with_inputs(content_data, criteria, ordering)


if __name__ == '__main__':
    manage_process()
