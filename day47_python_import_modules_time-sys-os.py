Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

import os
os.cpu_count()
12
os.environ
environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\Deepak kumar\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'LAPTOP-QEPM9I47', 'COMSPEC': 'C:\\windows\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'EFC_12020': '1', 'HOME': 'C:\\Users\\Deepak kumar', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\Deepak kumar', 'LOCALAPPDATA': 'C:\\Users\\Deepak kumar\\AppData\\Local', 'LOGONSERVER': '\\\\LAPTOP-QEPM9I47', 'NUMBER_OF_PROCESSORS': '12', 'ONEDRIVE': 'C:\\Users\\Deepak kumar\\OneDrive', 'ONEDRIVECONSUMER': 'C:\\Users\\Deepak kumar\\OneDrive', 'ONLINESERVICES': 'Online Services', 'OS': 'Windows_NT', 'PATH': 'C:\\Python310\\Scripts\\;C:\\Python310\\;C:\\windows\\system32;C:\\windows;C:\\windows\\System32\\Wbem;C:\\windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\windows\\System32\\OpenSSH\\;C:\\Users\\Deepak kumar\\AppData\\Local\\Microsoft\\WindowsApps;;C:\\Users\\Deepak kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\bin', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW', 'PLATFORMCODE': 'KV', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 154 Stepping 4, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '9a04', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'REGIONCODE': 'APJ', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\windows', 'TEMP': 'C:\\Users\\DEEPAK~1\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\DEEPAK~1\\AppData\\Local\\Temp', 'USERDOMAIN': 'LAPTOP-QEPM9I47', 'USERDOMAIN_ROAMINGPROFILE': 'LAPTOP-QEPM9I47', 'USERNAME': 'Deepak kumar', 'USERPROFILE': 'C:\\Users\\Deepak kumar', 'WINDIR': 'C:\\windows', 'ZES_ENABLE_SYSMAN': '1', '__PSLOCKDOWNPOLICY': '0'})
os.getcwd()
'C:\\Python310'
os.getlogin()
'Deepak kumar'
os.getpid()
392
os.getpid()
392

os.getppid()
19400

os.listdir('D:')
['$MfeDeepRem', '$RECYCLE.BIN', 'Mehh  !!!', 'Python Notes.docx', 'System Volume Information']
os.listdir('C:')
['calci_program.py', 'calci_program_using_init.py', 'counting_words_task7.1.py', 'creating_error_program.py', 'Daily task', 'day10_string_supporting_function_part_2.py', 'day11_decision_making_statements_part1.py', 'day13_lists_part1.py', 'day13_tuple_part2.py', 'day14_looping_for_loop.py', 'day15_whileloop&_control_flow_statements.py', 'day16_oops_part1.py', 'day17_oops_part2.py', 'day18_oops_part3.py', 'day19_set_listcontinuty.py', 'day1_python_intro.py', 'day20_set&dictinory.py', 'day21_right_triangle_using_for.py', 'day22_right_triangle_using_for_part2.py', 'day23_left_triangle_using_for.py', 'day24_row_column_printing.py', 'day25_database_part1.docx', 'day26_database_part2.py', 'day27_database_connection.py', 'day28_functions.py', 'day29_components_of_function.py', 'day2_tokens_part1.py', 'day30_math_functions.py', 'day31_user_defined_function.py', 'day32_functions_part2.py', 'day33_lambda_functions.py', 'day34_variable_in_oops.py', 'day35_inheritance.py', 'day36_inheritance_part2.py', 'day37_error&exception_theroy.py', 'day38_multithreading.py', 'day39_mulitthreading_life_cycle.py', 'day3_tokens_part2.py', 'day40_typesoferror.py', 'day41_regular_expression_part1.py', 'day42_regular_expression_part2.py', 'day43_regular_expression_part3.py', 'day44_modules.py', 'day4_tokens_operators_part_1.py', 'day5_tokens_operators_part_2.py', 'day6_string_management.py', 'day7_string_management_part_2.py', 'day8_formatting.py', 'day9_string_supporting_function.py', 'dbc_connection_program.py', 'DLLs', 'Doc', 'exception_err_program.py', 'fn.py', 'grade_program.py', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'polymorphism_program.py', 'python.exe', 'python3.dll', 'python310.dll', 'pythonw.exe', 'Scripts', 'share', 'tcl', 'Tools', 'vcruntime140.dll', 'vcruntime140_1.dll', 'web_platform_frameworks.py', 'weekly task', 'workout1.py', '__pycache__']

# this module will frunsih all details about OS

# sys module
# -----------

import sys
sys.api_version
1013

sys.builtin_module_names
('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections', '_contextvars', '_csv', '_datetime', '_functools', '_heapq', '_imp', '_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_pickle', '_random', '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', '_winapi', '_xxsubinterpreters', 'array', 'atexit', 'audioop', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'sys', 'time', 'winreg', 'xxsubtype', 'zlib')
sys.copyright
'Copyright (c) 2001-2023 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'

sys.flags
sys.flags(debug=0, inspect=0, interactive=0, optimize=0, dont_write_bytecode=0, no_user_site=0, no_site=0, ignore_environment=0, verbose=0, bytes_warning=0, quiet=0, hash_randomization=1, isolated=0, dev_mode=False, utf8_mode=0, warn_default_encoding=0, int_max_str_digits=-1)

sys.getwindowsversion()
sys.getwindowsversion(major=10, minor=0, build=22621, platform=2, service_pack='')

sys.hash_info
sys.hash_info(width=64, modulus=2305843009213693951, inf=314159, nan=0, imag=1000003, algorithm='siphash24', hash_bits=64, seed_bits=128, cutoff=0)
# machine optimisez sha algorithm , with python we using - siphash24 (Network programming or internet programming)

sys.int_info
sys.int_info(bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300, str_digits_check_threshold=640)

sys.maxunicode
1114111

chr(3000)
'ஸ'
chr(2979)
'ண'

# 1114111 --> stores all language , emoji and everthing in processor

print('\U0001f600')
😀
print('\U0001f601')
😁
print('\U0001f602')
😂
print('\U0001f604')
😄
print('\U0001f610')
😐
print('\U0001f645')
🙅
print('\U0001f532')
🔲

sys.path
['', 'C:\\Python310\\Lib\\idlelib', 'C:\\Python310\\python310.zip', 'C:\\Python310\\DLLs', 'C:\\Python310\\lib', 'C:\\Python310', 'C:\\Python310\\lib\\site-packages', 'C:\\Python310\\lib\\site-packages\\win32', 'C:\\Python310\\lib\\site-packages\\win32\\lib', 'C:\\Python310\\lib\\site-packages\\Pythonwin']
# this is NT path - network path

sys.platform
'win32'
sys.thread_info
sys.thread_info(name='nt', lock=None, version=None)

sys.version
'3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)]'
sys.version_info
sys.version_info(major=3, minor=10, micro=10, releaselevel='final', serial=0)

sys.winver
'3.10'

# time module
# -----------

import time

time.altzone
-23400

time.asctime()
'Tue Dec 12 12:05:16 2023'
time.ctime
<built-in function ctime>
>>> 
>>> time.ctime()
'Tue Dec 12 12:06:07 2023'
>>> 
>>> time.time()
1702362985.139346
>>> # epoch time scheme --> 1/1/1970 [ system default starting date ]
>>> 
>>> time.time(1)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    time.time(1)
TypeError: time.time() takes no arguments (1 given)
>>> time.ctime(1)
'Thu Jan  1 05:30:01 1970'
>>> time.ctime(2)
'Thu Jan  1 05:30:02 1970'
>>> 
>>> time.daylight
0
>>> time.gmtime()
time.struct_time(tm_year=2023, tm_mon=12, tm_mday=12, tm_hour=6, tm_min=47, tm_sec=29, tm_wday=1, tm_yday=346, tm_isdst=0)
>>> time.localtime()
time.struct_time(tm_year=2023, tm_mon=12, tm_mday=12, tm_hour=12, tm_min=18, tm_sec=13, tm_wday=1, tm_yday=346, tm_isdst=0)
>>> time.sleep(5)
>>> time.sleep(5)
>>> 
>>> time.timezone
-19800
>>> 19800/3600
5.5
>>> 
>>> time.tzname
('India Standard Time', 'India Daylight Time')
