integer_num=10
float_num=3.5
complex_num=10+3j

string_val="Hello Python"
list_val=[1,2,3,4]
tuple_val=(10,20,30,40)
range_val=range(5)

set_val={1,2,3,4}
frozenset_val=frozenset([1,2,3,4])
dict_val={"name":"Jacob","age":22}

bool_val=True
none_val=None

variables=[integer_num,float_num,complex_num,string_val,list_val,tuple_val,range_val,set_val,frozenset_val,dict_val,bool_val,none_val]

for val in variables:
    print(f"Value:{val},Type:{type(val)}")