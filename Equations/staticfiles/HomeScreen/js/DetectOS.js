async function detectOS() {
    let os = "Unknown";
    let version = "Unknown";
    
    if (navigator.userAgentData) {
        const uaData = await navigator.userAgentData.getHighEntropyValues([
            "platform",
            "platformVersion"
        ]);
  
        os = uaData.platform;
        version = uaData.platformVersion;
  
        if (os.includes("Chrome OS") || os.includes("Chromium OS")) {
            const match = navigator.userAgent.match(/CrOS [^ ]+ ([\d.]+)/);
            if (match) version = match[1];
        }
  
        if (os === "Windows" && parseInt(version.split(".")[0]) >= 13) {
            version = "11 (approx)";
        } else if (os === "Windows" && parseInt(version.split(".")[0]) < 13) {
            version = "10 or older (approx)";
        }
    } 
    else {
        const ua = navigator.userAgent;
    
        if (/Windows NT 10\.0/.test(ua)) {
            os = "Windows";
            version = "10 or 11 (indistinguishable)";
        } else if (/Mac OS X/.test(ua)) {
            os = "macOS";
            version = ua.match(/Mac OS X ([\d_]+)/)?.[1]?.replace(/_/g, ".") || "Unknown";
        } else if (/CrOS/.test(ua)) {
            os = "ChromeOS";
            version = ua.match(/CrOS [^ ]+ ([\d.]+)/)?.[1] || "Unknown";
        } else if (/Android/.test(ua)) {
            os = "Android";
            version = ua.match(/Android ([\d.]+)/)?.[1] || "Unknown";
        } else if (/iPhone|iPad|iPod/.test(ua)) {
            os = "iOS";
            version = ua.match(/OS ([\d_]+)/)?.[1]?.replace(/_/g, ".") || "Unknown";
        }
    }
  
    return {os, version};
}

async function main() {
    const info = await detectOS();

    let version = info.version
    let os = info.os
    let DerivedOSVersion = ""

    if (os === "Windows"){
        if (version === "10 or 11 (indistinguishable)"){
            //Do Nothing
        } else if (version.includes("(approx)")){
            DerivedOSVersion = version.slice(0,2); //makes Windows OS Version just the number (10 or 11)
        }
        let WindowsType = os + DerivedOSVersion;
        document.body.classList.add(WindowsType);
        console.log(WindowsType);
    } else if (["iOS", "Android", "ChromeOS", "macOS"].includes(os)){
        if (os === "iOS"){
            document.body.classList.add(iOS);
        } else if (os === "Android"){
            document.body.classList.add(Android);
        } else if (os === "ChromeOS"){
            document.body.classList.add(ChromeOS);
        } else if (os === "macOS"){
            document.body.classList.add(macOS);
        } else{
            document.body.classList.add(Linux)
        };
    };
};

main();