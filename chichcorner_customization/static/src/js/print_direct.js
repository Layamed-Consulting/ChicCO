/** @odoo-module **/
import { registry } from "@web/core/registry";

async function printAttachment(env, action) {
    try {
        if (action && action.params && action.params.html) {
            const reportHtml = action.params.html;
            console.log("Printing report from HTML content");

            const userAgent = navigator.userAgent || "";
            const isAndroid = /Android|iPhone|iPad|iPod/i.test(userAgent);

            if (isAndroid) {
                console.log("Android detected: Opening report in a new tab.");
                const newWindow = window.open("", "_blank");
                if (!newWindow) {
                    console.warn("Popup blocked! Enable popups to print automatically.");
                    return;
                }
                newWindow.document.open();
                newWindow.document.write(reportHtml);
                newWindow.document.close();
                newWindow.print();
                return;
            }


            let iframe = document.getElementById("printIframe");
            if (!iframe) {
                iframe = document.createElement("iframe");
                iframe.id = "printIframe";
                iframe.style.position = "absolute";
                iframe.style.width = "0px";
                iframe.style.height = "0px";
                iframe.style.border = "none";
                document.body.appendChild(iframe);
            }

            const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
            iframeDoc.open();
            iframeDoc.write(reportHtml);
            iframeDoc.close();

            iframe.onload = function () {
                console.log("Report Loaded, trying to print...");
                setTimeout(() => {
                    try {
                        iframe.contentWindow.print();
                    } catch (e) {
                        console.error("Print blocked due to security restrictions:", e);
                    }
                }, 1000);
            };
        } else {
            throw new Error("Report HTML content not provided or invalid");
        }
    } catch (error) {
        console.error("Error in printAttachment:", error);
    }
}

registry.category("actions").add("print_attachment", printAttachment);
