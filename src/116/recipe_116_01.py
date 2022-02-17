import configparser

# config 파일 로딩
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

# 값을 문자열로 얻는다
config['SAMPLE1']['str_key']

# config의 타입에 맞춰 값을 얻는다
str_value = config.get('SAMPLE1', 'str_key')
int_value = config.getint('SAMPLE1', 'int_key')
float_value = config.getfloat('SAMPLE2', 'float_key')
bool_value = config.getboolean('SAMPLE2', 'bool_key')

# 값을 표시한다
print(str_value)
print(int_value)
print(float_value)
print(bool_value)
