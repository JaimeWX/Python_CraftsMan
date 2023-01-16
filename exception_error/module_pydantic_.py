from pydantic import BaseModel, conint, ValidationError

class NumberInput(BaseModel):
    # 使用类型注解 conint 定义 number 属性的取值范围
    number: conint(ge=0, le=100)


def input_a_number_with_pydantic():
    while True:
        number = input('Please input a number (0-100): ')

        # 实例化为 pydantic 模型，捕获校验错误异常
        try:
            number_input = NumberInput(number=number)
        except ValidationError as e:
            print(e)
            continue

        number = number_input.number
        break

    print(f'Your number is {number}')

input_a_number_with_pydantic()