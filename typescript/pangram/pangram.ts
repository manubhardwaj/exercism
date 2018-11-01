class Pangram {
  private message: string = '';
  constructor(message: string = '') {
    this.message = message.toLowerCase();
  }

  isPangram() {
    let rePangram: RegExp = /([a-z])(?!.*\1)/g;
    return (this.message.match(rePangram) || []).length === 26;
    }
}

export default Pangram
