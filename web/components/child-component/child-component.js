class ChildComponent extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({mode: 'open'});
    }

    async connectedCallback() {
        this.shadowRoot.innerHTML = await fetch(import.meta.url.replace(".js", ".html")).then((response) => response.text());
        await this.load();
    }

    async load() {
        const timeout = setTimeout(() => {
            this.dataset.loaded = "true";
            clearTimeout(timeout);
        }, 2000);
    }

    async disconnectedCallback() {

    }
}

customElements.define('child-component', ChildComponent);