import { decode } from "../src/reto-02"

describe('first test', () =>{
    test("", () => {
        const message = "##*&"
        const expected = '4'
        const actual = decode(message)
        
        expect(actual).toBe(expected)
    })
})

describe('second test', () =>{
    test("", () => {
        const message = "&##&*&@&"
        const expected = '0243'
        const actual = decode(message)
        
        expect(actual).toBe(expected)
    })
})

describe('challenge', () =>{
    test("", () => {
        const message = "&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&"
        const expected = '024899455'
        const actual = decode(message)
        
        // console.log(actual)

        expect(actual).toBe(expected)
    })
})