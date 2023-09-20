import "./../child-component/child-component.js";

class ContainerComponent extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({mode: 'open'});
    }

    async connectedCallback() {
        this.shadowRoot.innerHTML = await fetch(import.meta.url.replace(".js", ".html")).then((response) => response.text());
        await this.load();
    }

    async load() {
        this.dataset.ready = "true";
    }

    async disconnectedCallback() {

    }
}

customElements.define('container-component', ContainerComponent);