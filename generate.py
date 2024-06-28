
def get_command_def(first, second):
  return "\\newcommand*{\\" + first + "}{\\" + second + "}\n"

mathcal_command = lambda s : "c" + s
mathcal_def = lambda s : "mathcal{" + s + "}"

mathbb_command = lambda s : s
mathbb_def = lambda s : "mathbb{" + s + "}"

mathfrak_command = lambda s : "f" + s
mathfrak_def = lambda s : "mathfrak{" + s + "}"

mathscr_command = lambda s : "s" + s
mathscr_def = lambda s : "mathscr{" + s + "}"

mathbf_command = lambda s : "b" + s
mathbf_def = lambda s : "mathbf{" + s + "}"

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_alphabets = "abcdefghijklmnopqrstuvwxyz"

with open("commands.tex", "a") as f:
  for i in range(26):
    f.write(get_command_def(mathbf_command(small_alphabets[i]), mathbf_def(small_alphabets[i])))
  pass