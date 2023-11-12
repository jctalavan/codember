export function decode(message:string) : string {
    let result : string = ""
    let currentValue: number = 0
    
    const chars = Array.from(message)

    chars.forEach(c => {
        switch(c){
            case "#": 
                currentValue += 1
                break
            case "@": 
                currentValue -= 1
                break
            case "*": 
                currentValue *= currentValue
                break
            case "&": 
                result = `${result}${currentValue}`
                break
        }
    })

    return result
}