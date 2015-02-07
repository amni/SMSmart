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
        MSG_SEGMENT_LENGTH = 140
        ERROR_CODE_MSG_LIMIT = '7'
        key_position = results.find(self.CARROT_TOKEN)
        key = results[:key_position]
        spliced_results = results[key_position+2:] #2 because the token is of length 2
        message_list = [spliced_results[i:i+MSG_SEGMENT_LENGTH] for i in range(0, len(spliced_results), MSG_SEGMENT_LENGTH)]
        return self.implement_standard_format(message_list, key)

    def implement_standard_format(self, results, key):
        MSG_COUNT_THRESHOLD = 15
        total_msg = len(results)
        messages_list=[]
        if len(messages_list) > MSG_COUNT_THRESHOLD:
            messages_list = ['(1/1)*']
            key = ERROR_CODE_MSG_LIMIT + key[1:]
        else: 
            for msg_number, message in enumerate(results):
                metadata = '(' + str(msg_number+1) + '/' + str(total_msg) + ')' + '*'
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
