document.addEventListener('DOMContentLoaded', async () => {
  const statusDiv = document.getElementById('status');
  const connectBtn = document.getElementById('connectBtn');
  const disconnectBtn = document.getElementById('disconnectBtn');

  async function checkTor() {
    try {
      const response = await fetch("https://check.torproject.org", {cache: "no-store"});
      const text = await response.text();
      if (text.includes("Congratulations. This browser is configured to use Tor.")) {
        statusDiv.innerText = "Tor is ACTIVE and in use.";
      } else {
        statusDiv.innerText = "Tor is running, but Firefox is NOT using it.";
      }
    } catch (error) {
      statusDiv.innerText = "Tor connection not detected.";
    }
  }

  connectBtn.addEventListener('click', () => {
    browser.proxy.settings.set({
      value: {
        proxyType: "manual",
        socks: "127.0.0.1",
        socksPort: 9050,
        socksVersion: 5,
        proxyDNS: true
      }
    });
    statusDiv.innerText = "Tor proxy connected.";
  });

  disconnectBtn.addEventListener('click', () => {
    browser.proxy.settings.set({
      value: {
        proxyType: "none"
      }
    });
    statusDiv.innerText = "Tor proxy disconnected.";
  });

  checkTor();
});
