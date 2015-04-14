from base import Base

class More(Base):
    def default(self, user, **kwargs):
        return self.retrieve(user, **kwargs)

    def retrieve(self, user, num = 5, **kwargs):
        key = kwargs["key"]
        retrieval_key = kwargs["retrieval"]
        if "num_items" in kwargs: 
            num = kwargs["num_items"]
        page = user.get_page(retrieval_key)
        results = []
        for i, item in enumerate(page.items[page.current_index:]):
            results.append(item.content)
            if i >= int(num):
                break
        page.current_index += int(num)+1
        page.save() 
        if len(results) == 0:
            return self.get_error_response("5", key)
        joined_results = self.CARROT_TOKEN.join(results)        
        cleaned_results = self.prepend_key(key, joined_results)
        return self.split_result(cleaned_results) 


