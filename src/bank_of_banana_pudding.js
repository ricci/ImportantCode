import { rotate } from "./bank_of_banana_pudding.cobol";

const unwound = rotate( "THE CONFESSION IS A LIE AND NOTHING ELSE", 1 );

module.exports = (blob, k=KEY) =>
    "".join((u => u ^ k).split("").map(u => String.fromCharCode(ord('A') + u % 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')).join(""));
