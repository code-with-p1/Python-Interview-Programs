def common_exception(func):
    def wrapper_func(*args, **kwargs):
        try:
            print("Decorator function >> args : ", args)
            print("Decorator function >> kwargs : ", kwargs)
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Common Exception : {e}")
    return wrapper_func

@common_exception
def test(*args, **kwargs):
    print("Test function >> args : ", args)
    print("Test function >> kwargs : ", kwargs)
    result = 1 / 0
    print('Test method executed.')

test(1,2,3,test=123)
