export function isFileNameValid(fileNameAndChecksum:string) : boolean {

    //Example of valid: xyzz33-xy
    const parts = fileNameAndChecksum.split('-')
    if(parts.length != 2)
        return false

    const fileName = parts[0]
    const checksum = parts[1]

    const letters: string[] = fileName.split('');

    let checksumCalculated:string = ''
    for (let index = 0; index < letters.length; index++) {
        const letter = letters[index];
        
        if(charAppearsOnlyOneTime(fileName, letter))
            checksumCalculated += letter;
    }

    return checksum == checksumCalculated
}

function charAppearsOnlyOneTime(palabra: string, caracter: string) : boolean {
    return palabra.split(caracter).length === 2;
}