from models import User

class Base(object):
    OK = '0'
    EMPTY_MSG = ' '
    TRUE_TOKEN = 'T'
    CARROT_TOKEN = '^^'
    GEO_TOKEN = '#'
    SEPARATOR_TOKEN = '||'

    def find_results(self, **kwargs):
        pass

    def is_error(self, response):
        return isinstance(response, str) and len(response) == 1 

    def get_error_response(self, results, key):
        result = results + key + self.CARROT_TOKEN + self.EMPTY_MSG
        return self.split_result(result)

    def split_result(self, results):
        MSG_SEGMENT_LENGTH = 130
        MSG_COUNT_THRESHOLD = 9
        ERROR_CODE_MSG_LIMIT = '7'
        messages_list = []
        key_position = results.find(self.CARROT_TOKEN)
        key = results[:key_position]
        results = results[key_position+2:] #2 because the token is of length 2
        position = 0
        remainder = len(results)
        msg_number = 1
        temp = remainder/MSG_SEGMENT_LENGTH
        total_msg = temp + 1 if (remainder%MSG_SEGMENT_LENGTH != 0) else temp
        while remainder > MSG_SEGMENT_LENGTH:
            message = results[position:position+MSG_SEGMENT_LENGTH]
            metadata = '(' + str(msg_number) + '/' + str(total_msg) + ')' + '*'
            msg_number += 1        
            remainder -= MSG_SEGMENT_LENGTH
            position += MSG_SEGMENT_LENGTH
            messages_list.append(metadata+message)
        if remainder > 0:
            message = results[position:]
            metadata = '(' + str(msg_number) + '/' + str(total_msg) + ')' + '*'
            msg_number += 1   
            messages_list.append(metadata+message)
        if len(messages_list) > MSG_COUNT_THRESHOLD:
            messages_list = ['(1/1)*']
            key = ERROR_CODE_MSG_LIMIT + key[1:]
        return {"messages":messages_list, "key": key}

    def save(self, user, results):
        new_query = Query(response = results)
        return new_query

    def get_result_list(self, key, results):
        delimited_results = self.CARROT_TOKEN.join(results)
        return self.prepend_key(key, delimited_results)

    def prepend_key(self, key, results):
        return self.OK+key+self.CARROT_TOKEN+results
