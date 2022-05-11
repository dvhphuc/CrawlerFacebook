def normstring(s):
    words = s.split('/')
    if words[4]=='posts':
        text = words[5]
    return text[0:text.find('?')]

print(normstring("https://www.facebook.com/ConfessionUIT/posts/pfbid0d9ZMThZaTtcFc4z5iGvv3s7DCVKAmsp2WewVVb4ek81rZTYGjQNnQ69B9PzeJH6dl?__cft__[0]=AZWOEOHhE1UHK5Lw-JJXFIXf66gOCiFdRR6Z3dlYrvaUFzLQEUhysO4zaWuNmcu4xOeM3knVZVKcEHQ7Xs2GsgDIu_ao27BZvXZpuTXNg2DF6C_1gFfe0RyoMe5EqoNSm_z34DoTGEA38LLq7bRlmiZTyp1BZuT3-HIFMQyh4Nvgsw&__tn__=%2CO%2CP-R"))
