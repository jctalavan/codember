export function GetFirtsLetterOfUsernameForInvalidEntries(db: Array<string>): string{
    let result: string = ''

    for (let index = 0; index < db.length; index++) {
        const element = db[index];
        
        const elementParts = element.split(',')

        if(!isValidElement(elementParts))
            result += elementParts[0].charAt(0)
    }

    return result
}

function isValidElement(parts : Array<string>) : boolean {


    if(parts.length != 5)
        return false

    if(!isValidId(parts[0]))
        return false
    
    if(!isValidUsername(parts[1]))
        return false
    
    if(!isValidEmail(parts[2]))
        return false
        
    if(!isValidAge(parts[3]))
        return false

    if(!isValidLocation(parts[4]))
        return false

    return true
}

function isValidId (id: string) : boolean{
    // - id: exists and is alphanumeric
    return true
}

function isValidUsername (username: string) : boolean{
    // - username: exists and is alphanumeric
    return true
}

function isValidEmail (email: string) : boolean{
    // - email: exists and is valid (follows the pattern user@domain.com)
    return true
}

function isValidAge (age: string) : boolean{
    // - age: is optional but if it appears it is a number
    
    if(age === '') return true

    return true
}

function isValidLocation (location: string) : boolean{
    // - location: is optional but if it appears it is a text string
    if(location === '') return true

    return true
}