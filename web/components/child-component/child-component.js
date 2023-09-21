class ChildComponent extends HTMLElement {
    #clickHandler = this.#click.bind(this)

    constructor() {
        super();
        this.attachShadow({mode: 'open'});
    }

    async connectedCallback() {
        this.dataset.loading = "true";
        this.shadowRoot.innerHTML = await fetch(import.meta.url.replace(".js", ".html")).then((response) => response.text());
        await this.load();
    }

    async load() {
        const timeout = setTimeout(() => {
            this.shadowRoot.querySelector("button").addEventListener("click", this.#clickHandler);
            delete this.dataset.loading;
            this.dataset.ready = "true";
            clearTimeout(timeout);
        }, 2000);
    }

    async disconnectedCallback() {

    }

    async #click(event) {
        const target = event.composedPath()[0];
        target.textContent = "clicked";

        delete this.dataset.ready;
        const timeout = setTimeout(() => {
            this.dataset.ready = "true";
            clearTimeout(timeout);
        }, 2000);
    }
}

customElements.define('child-component', ChildComponent);