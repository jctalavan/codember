import { isKeyValid, getInvalidKeyAtPositionN } from "../src/reto-03"

describe('Valid Key', () =>{
    test("", () => {
        const key = "2-4 f: fgff"
        const expected = true
        const actual = isKeyValid(key)
        
        expect(actual).toBe(expected)
    })
})

describe('Invalid Key', () =>{
    test("", () => {
        const key = "4-6 z: zzzsg"
        const expected = false
        const actual = isKeyValid(key)
        
        expect(actual).toBe(expected)
    })
})

describe('Invalid Key at position 42', () =>{
    test("", async () => {
        const expected = '9-10 d: bgamidqewtbus'

        let url = 'https://codember.dev/data/encryption_policies.txt';
        
        const txt = await fetch(url)
            .then(response => response.text())
            .then(t => t);
        
        const keys = txt.split('\n');
        
        const actual = getInvalidKeyAtPositionN(keys, 42)
        
        expect(actual).toBe(expected)
    })
})