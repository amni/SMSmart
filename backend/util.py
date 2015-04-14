
class PhoneNumbersUtil():
    PHONE_NUMBERS_US = ["+14159856984", "+19195848629", "+14082143089", "+15733093911", "+15852285686"]
    PHONE_NUMBERS_UK = ["+447441906017", "+447441906514", "+447441906376", "+447441906383", "+447441906394"]
    PHONE_NUMBERS_CA = ["+12894320286", "+15813183824", "+14184781054", "+15877824197", "+12893520921"]

    PHONE_NUMBERS = {'US':PHONE_NUMBERS_US, 'UK': PHONE_NUMBERS_UK, 'CA': PHONE_NUMBERS_CA, 'GB': PHONE_NUMBERS_UK}

    # given country code, give the appropriate next number 
    def get_phone_number(self, country_code):
        numbers = self.PHONE_NUMBERS[country_code]
        from_number = numbers.pop(0)
        numbers.append(from_number)
        self.PHONE_NUMBERS[country_code] = numbers
        return from_number
