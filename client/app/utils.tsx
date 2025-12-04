// Description: Utility function to generate a UUID.
export function generateUUID(): string {
    const hexChars = '0123456789abcdef';
    let result = '';
    for (let i = 0; i < 24; i++) {
    result += hexChars[Math.floor(Math.random() * 16)];
    }
    return result;
}