"use strict";
exports.__esModule = true;
var pangram_1 = require("./pangram");
describe('Pangram()', function () {
    it('empty sentence', function () {
        var pangram = new pangram_1["default"]('');
        expect(pangram.isPangram()).toBe(false);
    });
    it('pangram with only lower case', function () {
        var pangram = new pangram_1["default"]("the quick brown fox jumps over the lazy dog");
        expect(pangram.isPangram()).toBe(true);
    });
    it("missing character 'x'", function () {
        var pangram = new pangram_1["default"]("a quick movement of the enemy will jeopardize five gunboats");
        expect(pangram.isPangram()).toBe(false);
    });
    it("another missing character 'x'", function () {
        var pangram = new pangram_1["default"]("the quick brown fish jumps over the lazy dog");
        expect(pangram.isPangram()).toBe(false);
    });
    it("pangram with underscores", function () {
        var pangram = new pangram_1["default"]("the_quick_brown_fox_jumps_over_the_lazy_dog");
        expect(pangram.isPangram()).toBe(true);
    });
    it("pangram with numbers", function () {
        var pangram = new pangram_1["default"]("the 1 quick brown fox jumps over the 2 lazy dogs");
        expect(pangram.isPangram()).toBe(true);
    });
    it('missing letters replaced by numbers', function () {
        var pangram = new pangram_1["default"]("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog");
        expect(pangram.isPangram()).toBe(false);
    });
    it('pangram with mixed case and punctuation', function () {
        var pangram = new pangram_1["default"]("\"Five quacking Zephyrs jolt my wax bed.\"");
        expect(pangram.isPangram()).toBe(true);
    });
    it('pangram with non-ascii characters', function () {
        var pangram = new pangram_1["default"]("Victor jagt zwölf Boxkämpfer quer über den großen Sylter Deich.");
        expect(pangram.isPangram()).toBe(true);
    });
});
