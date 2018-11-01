class Bob {
    hey(input: string): string {
        switch (true) {
            case this.isYelling(input):
                return 'Whoa, chill out!'
            case this.isQuestioning(input):
                return 'Sure.'
            case this.isSilent(input):
                return 'Fine. Be that way!'
            default:
                return 'Whatever.'
        }
    }

    isQuestioning(input: string): boolean {
        return input.endsWith('?')
    }

    isYelling(input: string): boolean {
        return (input.match(/[A-Z]/) != null) && input == input.toUpperCase();
    }

    isSilent(input: string): boolean {
        return input.trim().length == 0;
    }

}

export default Bob
