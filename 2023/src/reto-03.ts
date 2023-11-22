export function getInvalidKeyAtPositionN(keys: Array<string>, numberOfInvalidKey: number) : string {

    let counter:number  = 0;
    
    for (let index = 0; index < keys.length; index++) {
        const key = keys[index];
        
        if(!isKeyValid(key))
            counter++;
    
        if(counter === numberOfInvalidKey)
            return key;
    }

    return ''
}

export function isKeyValid(key: string) : boolean{
    
    const keyObj:KeyParts = new KeyParts(key)

    const letters: string[] = keyObj.keyToCheck.split('');

    const appareances = letters.filter(letter => letter === keyObj.letter).length

    return appareances >= keyObj.minAppareances && appareances <= keyObj.maxAppareances
}

class KeyParts {
    //8-10 r: ozrcdfnug

    minAppareances:number;
    maxAppareances:number;
    letter:string;
    keyToCheck:string;

    constructor(key:string){
        const parts: string[] = key.split(':')
        const part_0: string[] = parts[0].split(' ')
        const part_0_0: string[] = part_0[0].split('-')

        this.minAppareances = parseInt(part_0_0[0])
        this.maxAppareances = parseInt(part_0_0[1])
        this.letter = part_0[1]
        this.keyToCheck = parts[1].trim()
    }

}