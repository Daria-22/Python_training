love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
love_maybe_lines_stripped = []

for i in love_maybe_lines:
  stripped_i = i.strip();
  love_maybe_lines_stripped.append(stripped_i)
print(love_maybe_lines_stripped)
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)