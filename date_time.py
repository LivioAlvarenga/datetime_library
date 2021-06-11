
def time_greet(format: str = 't', idioma: str = 'br') -> str:
    """Retorno comprimentos de bom dia, boa tarde e boa noite em portugues e
    em inglês.

        Args:
            format(str): t para title (Bom dia) - u para upper (BOM DIA) - l
            para lower (bom dia).
                padrão = 't'

            idioma(str): br para portugues Brasil - en para inglês.
                padrão = 'br'

        Returns:
            if 6 <= hora < 12:
                'Bom dia'
            if 12 <= hora < 18:
                'Boa tarde'
            else:
                'Boa noite'
    """
    from datetime import datetime

    format = format.lower()
    idioma = idioma.lower()
    agora = datetime.now().hour

    if 6 <= agora < 12:

        if idioma == 'br':
            greet = 'bom dia' if format == 'l' else 'BOM DIA' \
                if format == 'u' else 'Bom dia'
        elif idioma == 'en':
            greet = 'good morning' if format == 'l' else 'GOOD MORNING' \
                if format == 'u' else 'Good morning'

    elif 12 <= agora < 18:

        if idioma == 'br':
            greet = 'boa tarde' if format == 'l' else 'BOA TARDE' \
                if format == 'u' else 'Boa tarde'
        elif idioma == 'en':
            greet = 'good afternoon' if format == 'l' else 'GOOD AFTERNOON' \
                if format == 'u' else 'Good afternoon'

    else:
        if idioma == 'br':
            greet = 'boa noite' if format == 'l' else 'BOA NOITE' \
                if format == 'u' else 'Boa noite'
        elif idioma == 'en':
            greet = 'good evening' if format == 'l' else 'GOOD EVENING' \
                if format == 'u' else 'Good evening'

    return greet


# .Testando o código.
if __name__ == '__main__':
    greet = time_greet()
    print(greet)

    greet = time_greet('L')
    print(greet)

    greet = time_greet('u')
    print(greet)

    greet = time_greet('T', 'en')
    print(greet)

    greet = time_greet('l', 'En')
    print(greet)

    greet = time_greet('U', 'EN')
    print(greet)
