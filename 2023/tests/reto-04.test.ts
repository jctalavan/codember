import { isFileNameValid } from "../src/reto-04";

describe('Valid checksum', () =>{
    test("", () => {
        const fileNameAndChecksum = "xyzz33-xy"
        const expected = true
        const actual = isFileNameValid(fileNameAndChecksum)
        
        expect(actual).toBe(expected)
    })
})

describe('Invalid checksum', () =>{
    test("", () => {
        const fileNameAndChecksum = "abcca1-ab1"
        const expected = false
        const actual = isFileNameValid(fileNameAndChecksum)
        
        expect(actual).toBe(expected)
    })
})

describe('Valid FileName at position 33', () =>{
    test("", async () => {
        const expectedPosition = 33

        let url = 'https://codember.dev/data/files_quarantine.txt';
        
        const txt = await fetch(url)
            .then(response => response.text())
            .then(t => t);
        
        const items = txt.split('\n');
        
        let counter:number = 0
        let solution:string = ''
        for (let index = 0; index < items.length; index++) {
            const fileNameAndChecksum = items[index];
            
            if(isFileNameValid(fileNameAndChecksum))
                counter++;

            if(counter == expectedPosition)
                solution = fileNameAndChecksum
        }

        expect(counter).toBeGreaterThan(expectedPosition)
        expect(solution).toBe('O2hrQ-O2hrQ')
    })
})