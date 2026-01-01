import net;
import crypto;
import sys;

class SecurityTool {
    function scanTarget(host: string, startPort: int, endPort: int) {
        print("Starting scan on " + host);
        for port in startPort..endPort {
            if net.scan(host, port) {
                print("Port " + port + " is OPEN");
            }
        }
    }

    function secureHash(password: string): string {
        let salt = "E_SHARP_SALT_2026";
        return crypto.hash_sha256(password + salt);
    }
}

let tool = SecurityTool();

// 1. Network Scan Simulation
tool.scanTarget("127.0.0.1", 79, 81);

// 2. Cryptography
let myHash = tool.secureHash("admin123");
print("Secure Hash: " + myHash);

// 3. System Info
print("System OS Info:");
print(sys.execute("uname -a"));
