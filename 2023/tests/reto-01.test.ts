import { decrypt } from "../src/reto-01";

describe('first test', () =>{
    test("", () => {
        const message = 'keys house HOUSE house keys'
        const expected = 'keys2house3'
        const actual = decrypt(message)
        
        expect(actual).toBe(expected)
    })
})

describe('second test', () =>{
    test("", () => {
        const message = 'cup te a cup'
        const expected = 'cup2te1a1'
        const actual = decrypt(message)
        
        expect(actual).toBe(expected)
    })
})

describe('third test', () =>{
    test("", () => {
        const message = 'houses house housess'
        const expected = 'houses1house1housess1'
        const actual = decrypt(message)
        
        expect(actual).toBe(expected)
    })
})