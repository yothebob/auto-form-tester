import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

browser = webdriver.Firefox()
browser.get("https://www.google.com")
#{id|id_name OR name|field_name : [type, value]}
form_values = {
    # "id|username" : ['text' ,'brandon'],
    # "id|password" : ['text' ,'password'],
    "name|q" : ['text',"hello world"],
    "name|btnK" : ['submit']
}
 
def fulfill_form(form_values):
    for field_id, value in form_values.items():
            
        type_label = field_id.split("|")
        if len(type_label) == 2:
            if type_label[0].lower() == "id":
                elem = browser.find_element(By.ID, type_label[1])
                if value[0].lower() =="submit":
                    print("Submitting form!")
                    elem.click()
                elem.send_keys(value[-1] + Keys.RETURN)

            if type_label[0].lower() == "name":
                print(f"going to {type_label[1]}!")
                elem = browser.find_element(By.NAME, type_label[1])
                if value[0].lower() =="submit":
                    print("Submitting form!")
                    elem.click()
                elem.send_keys(value[-1] + Keys.RETURN)
        else:
             print(f"there is something wrong with your value {field_id}, do id|id_name or name|field_name")


def cli():
    form_values = {}
    more_form_values = True
    while more_form_values:
        _new_val = input("input new value EX 'id|id_value' OR 'name|name_value':\n")
        _form_type = input("what is the field type? \n 1 : text, 2 : submit")
        if form_type != "1" or form_type != "2":
            _form_type = input("what is the field type? \n 1 : text, 2 : submit")
        else:
            if form_type != "2":
                _form_value = input("what is the disired value?: ")
                form_type.append(_form_type)
                form_type.append(_form_value)
            else:
                form_type.append(_form_type)
        form_values[_new_val] = form_type
        _more_data = input("Do you have more to add?(y/n)")
        more_form_values = True if _more_data == "y" else False
    fulfill_form(form_values)

    
def import_from_json(json_file):
    with open(json_file, "r") as jf:
        jfr = jf.read()
        form_values = json.loads(jfr)
        fulfill_form(form_values)
