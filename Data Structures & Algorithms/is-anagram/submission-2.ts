class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length) return false

        const shash: {string?: number} = {}
        const thash: {string?: number} = {}

        for (let i = 0; i < s.length; i++){
            if (Object.hasOwn(shash, s[i])) shash[s[i]]++
            else shash[s[i]] = 1
            if (Object.hasOwn(thash, t[i])) thash[t[i]]++
            else thash[t[i]] = 1

        }
        console.log(shash, thash)
        for (const key of Object.keys(shash)){
            if (!Object.hasOwn(thash, key) || shash[key] !== thash[key]) return false
        }

        return true
    }
}
