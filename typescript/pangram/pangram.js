"use strict";
exports.__esModule = true;
var Pangram = /** @class */ (function () {
    function Pangram(message) {
        if (message === void 0) { message = ''; }
        this.message = '';
        this.message = message.toLowerCase();
    }
    Pangram.prototype.isPangram = function () {
        var rePangram = /([a-z])(?!.*\1)/g;
        return (this.message.match(rePangram) || []).length === 26;
    };
    return Pangram;
}());
exports["default"] = Pangram;
