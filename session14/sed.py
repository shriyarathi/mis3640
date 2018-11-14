def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.
    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    pass


pattern = 'man'
replace = 'woman'
source = 'output.txt'
dest = 'new_' + source
sed(pattern, replace, source, dest)



