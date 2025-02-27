import sys
from pprint import pprint

from mail import send_email as send, self_test
from parse import get_data, parse_name, parse_id, check_exist
from passwd import rand_pass
from constant import CSV_NAME_FIELD, CSV_ID_FIELD, SUBJECT_TEMPLATE, BODY_TEMPLATE, RECIPIENT_TEMPLATE, CLASS_NAME, WEBSITE, OUTPUT_CSV_FN

def main():
    data = get_data(CSV_NAME_FIELD, CSV_ID_FIELD)
    import_csv = open(OUTPUT_CSV_FN, "w", encoding='utf-8')
    for d in data:
        name = d[CSV_NAME_FIELD] = parse_name(d[CSV_NAME_FIELD])
        account = d[CSV_ID_FIELD] = parse_id(d[CSV_ID_FIELD])
        d["exist"] = check_exist(d[CSV_ID_FIELD])
        pprint(d, stream=sys.stderr)
        if not d["exist"]:
            password = rand_pass()
            subject = SUBJECT_TEMPLATE.substitute(
                    CLASS_NAME=CLASS_NAME
            )
            body = BODY_TEMPLATE.substitute(
                    NAME=name,
                    CLASS_NAME=CLASS_NAME,
                    WEBSITE=WEBSITE,
                    ACCOUNT=account,
                    PASSWORD=password
            )
            recipient = RECIPIENT_TEMPLATE.substitute(
                    ACCOUNT=account
            )
            print(f"\"{account}\",\"{password}\",\"{recipient}\",\"{name}\"", file=import_csv)
            send(subject, body, recipient)
    import_csv.close()

if __name__ == '__main__':
    main()
