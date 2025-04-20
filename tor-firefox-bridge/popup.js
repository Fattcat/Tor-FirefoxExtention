function showMessage(message, isSuccess = true) {
  const msgBox = document.createElement("div");
  msgBox.textContent = message;
  msgBox.className = isSuccess ? "msg success" : "msg error";
  document.body.appendChild(msgBox);

  setTimeout(() => {
    msgBox.remove();
  }, 4000);
}

function updateTorStatus(isTorActive) {
  const statusElem = document.getElementById('tor-status');
  if (isTorActive) {
    statusElem.textContent = "✅ Tor network is active.";
    statusElem.style.color = "lightgreen";
  } else {
    statusElem.textContent = "❌ Tor network is not active.";
    statusElem.style.color = "red";
  }
}

function checkTorStatus() {
  fetch("https://check.torproject.org/")
    .then(res => res.text())
    .then(html => {
      updateTorStatus(html.includes("Congratulations. This browser is configured to use Tor."));
    })
    .catch(() => {
      updateTorStatus(false);
    });
}

// Init: spustí sa hneď pri otvorení rozšírenia
checkTorStatus();

document.getElementById("connectBtn").addEventListener("click", () => {
  chrome.proxy.settings.set(
    {
      value: {
        mode: "fixed_servers",
        rules: {
          proxyForHttp: { scheme: "socks5", host: "127.0.0.1", port: 9050 },
          proxyForHttps: { scheme: "socks5", host: "127.0.0.1", port: 9050 },
          bypassList: ["localhost"]
        }
      },
      scope: "regular"
    },
    () => {
      showMessage("Firefox is now routed through Tor.", true);
      setTimeout(() => {
        checkTorStatus();  // 💡 Voláme znova kontrolu stavu po prepnutí proxy
      }, 1500); // necháme Tor chvíľu prepnúť
    }
  );
});

document.getElementById("disconnectBtn").addEventListener("click", () => {
  chrome.proxy.settings.clear({ scope: "regular" }, () => {
    showMessage("Firefox is now disconnected from Tor.", false);
    setTimeout(() => {
      checkTorStatus(); // znova overíme, či sa vrátil do normálneho režimu
    }, 1500);
  });
});
