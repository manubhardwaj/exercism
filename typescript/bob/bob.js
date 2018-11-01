"use strict";
exports.__esModule = true;
var Bob = /** @class */ (function () {
    function Bob() {
    }
    Bob.prototype.hey = function (input) {
        switch (true) {
            case this.isYelling(input):
                return 'Whoa, chill out!';
            case this.isQuestioning(input):
                return 'Sure.';
            case this.isSilent(input):
                return 'Fine. Be that way!';
            default:
                return 'Whatever.';
        }
    };
    Bob.prototype.isQuestioning = function (input) {
        return input.endsWith('?');
    };
    Bob.prototype.isYelling = function (input) {
        return (input.match(/[A-Z]/) != null) && input == input.toUpperCase();
    };
    Bob.prototype.isSilent = function (input) {
        return input.trim().length == 0;
    };
    return Bob;
}());
exports["default"] = Bob;
