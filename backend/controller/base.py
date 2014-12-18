from models import User

class Base(object):
    def find_results(self, **kwargs):
        pass

    def split_result(self, results):
            MSG_SEGMENT_LENGTH = 150
            messages_list = []
            key_position = results.find('^')
            key = results[:key_position]
            results = results[key_position+1:]
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
            return {"messages":messages_list, "key": key}

    def save(self, user, results):
        new_query = Query(response = results)
        return new_query
