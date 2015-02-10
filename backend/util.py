
class PhoneNumbersUtil():
    PHONE_NUMBERS_US = ["+14159856984", "+19195848629", "+14082143089", "+15733093911", "+15852285686"]
    PHONE_NUMBERS_UK = ["+447441906017"]

    PHONE_NUMBERS = {'1':PHONE_NUMBERS_US, '44': PHONE_NUMBERS_UK}

    # given country code, give the appropriate next number 
    def get_phone_number(self, country_code):
        numbers = self.PHONE_NUMBERS[country_code]
        from_number = numbers.pop(0)
        numbers.append(from_number)
        self.PHONE_NUMBERS[country_code] = numbers
        return from_number

