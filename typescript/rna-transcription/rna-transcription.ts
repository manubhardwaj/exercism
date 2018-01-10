// Thanks @jaemk

class Transcriptor {
    private conv(s: string): string | undefined {
        switch (s) {
            case 'A': return 'U'
            case 'T': return 'A'
            case 'G': return 'C'
            case 'C': return 'G'
            default: return undefined
        }
    }
    toRna(seq: string) {
        let rna = ''
        for (const c of seq) {
            const piece = this.conv(c)
            if (!piece) { throw('Invalid input DNA.') }
            rna += piece
        }
        return rna
    }
}

export default Transcriptor

