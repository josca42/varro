# Disclosure (Accordion) Component - Alpine.js

## Installation

To use this component, you will need the pre-released Alpine UI plugin included via cdn. Make sure to include it BEFORE Alpine core JS file.

```html
<script defer src="https://unpkg.com/@alpinejs/ui@3.15.3/dist/cdn.min.js"></script>
<script defer src="https://unpkg.com/@alpinejs/collapse@3.15.3/dist/cdn.min.js"></script>
<script defer src="https://unpkg.com/alpinejs@3.15.3/dist/cdn.min.js"></script>
```

## A Basic Example

```html
<div x-data>
    <div x-disclosure>
        <button x-disclosure:button>Question #1</button>

        <div x-disclosure:panel>
            Lorem ipsum dolor sit...
        </div>
    </div>

    <div x-disclosure>
        <button x-disclosure:button>Question #2</button>

        <div x-disclosure:panel>
            Lorem ipsum dolor sit...
        </div>
    </div>
</div>
```

## Styling based on the open state

You can apply custom styling to the selected disclosure by using the $disclosure.isOpen boolean and setting any classes you need.

```html
<div x-data>
    <div x-disclosure>
        <button x-disclosure:button :class="$disclosure.isOpen && 'bg-gray-200'">Trigger</button>

        <div x-disclosure:panel>
            ...
        </div>
    </div>
</div>
```

## Using x-collapse for smooth transitions

The Collapse Plugin works great in combination with x-disclosure:panel. Install the plugin, then add x-collapse to any x-disclosure:panel element to get smooth height transitions.

```html
<div x-data>
    <div x-disclosure>
        <button x-disclosure:button>Trigger</button>

        <div x-disclosure:panel x-collapse>
            ...
        </div>
    </div>
</div>
```

## Specifying the default open state

You can specify the default open state when the page loads by using the default-open attribute on the x-disclosure element.

```html
<div x-data>
    <div x-disclosure default-open>
        <button x-disclosure:button>Trigger</button>

        <div x-disclosure:panel>
            ...
        </div>
    </div>
</div>
```

## Closing disclosures manually

If you wish to programatically close the disclosure, you can do so using the $disclosure.close() method anywhere inside the x-disclosure element.

```html
<div x-data>
    <div x-disclosure>
        <button x-disclosure:button>Trigger</button>

        <div x-disclosure:panel>
            ...
            <button type="button" x-on:click="$disclosure.close()">
                Close
            </button>
        </div>
    </div>
</div>
```

## API Reference

### x-disclosure

The main directive for the Disclosure component, used to contain the behavior for a disclosure, button, and panel.

| Attributes | Description |
|------------|-------------|
| default-open | A boolean to set the default open state |

### x-disclosure:button

Used to specify the button that toggles the disclosure.

### x-disclosure:panel

Used to specify the panel that will be toggled.

### $disclosure

A magic variable that exposes information about the current state of the disclosure and enables programatically closing the disclosure.

| Properties | Description |
|------------|-------------|
| isOpen | A boolean used to determine whether or not the disclosure is currently open |
| close | A method used to programatically close the disclosure |