import re


class Controller:
    def isValid(self, card_number):
        if len(card_number) != 16 and len(card_number) != 19:
            return "Invalid"

        if len(card_number) == 16:
            if re.search("[456][0-9]{15}", card_number) is None:
                return "Invalid"

        if len(card_number) == 19:
            if re.search("[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}", card_number) is None:
                return "Invalid"

        card_number = card_number.replace("-", "")
        previous = card_number[0]
        count = 0

        for current in card_number[1:16]:
            if current == previous:
                count += 1
                if count >= 3:
                    return "Invalid"
            else:
                count = 0

            previous = current

        return "Valid"
