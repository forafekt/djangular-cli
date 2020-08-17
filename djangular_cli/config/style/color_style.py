from djangular_cli.terminal import style_from_dict

from djangular_cli.terminal import Token

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: 'bold',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '#673AB7 bold',
    Token.Exit: '#2196f3 bold',
})
