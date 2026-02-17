# Combobox (Autocomplete) Component - Alpine.js

## Installation

To use this component, you will need the pre-released Alpine UI plugin included via cdn. Make sure to include it BEFORE Alpine core JS file.

```html
<script defer src="https://unpkg.com/@alpinejs/ui@3.15.3/dist/cdn.min.js"></script>
<script defer src="https://unpkg.com/@alpinejs/focus@3.15.3/dist/cdn.min.js"></script>
<script defer src="https://unpkg.com/alpinejs@3.15.3/dist/cdn.min.js"></script>
```

## A Basic Example

```html
<div x-data="{
    query: '',
    selected: null,
    frameworks: [
        { id: 1, name: 'Laravel', disabled: false },
        { id: 2, name: 'Ruby on Rails', disabled: false },
        { id: 3, name: 'Django', disabled: false },
    ],
    get filteredFrameworks() {
        return this.query === ''
            ? this.frameworks
            : this.frameworks.filter((framework) => {
                return framework.name.toLowerCase().includes(this.query.toLowerCase())
            })
    },
}">
    <div x-combobox x-model="selected">
        <label x-combobox:label>Select framework</label>

        <input x-combobox:input
               :display-value="framework => framework.name"
               @change="query = $event.target.value;"
               placeholder="Search..."
        />

        <button x-combobox:button>Toggle</button>

        <ul x-combobox:options>
            <template x-for="framework in filteredFrameworks" :key="framework.id">
                <li x-combobox:option
                    :value="framework"
                    :disabled="framework.disabled">
                    <span x-text="framework.name"></span>
                </li>
            </template>
        </ul>
    </div>
</div>
```

## Styling the selected, active, and disabled items

You can apply custom styling to the selected, active, and disabled items by using the $comboboxOption.isSelected, $comboboxOption.isActive, and $comboboxOption.isDisabled booleans respectively and setting any classes you need.

```html
<li x-combobox:option
    :class="{
        'bg-cyan-500/10': $comboboxOption.isActive,
        'opacity-50 cursor-not-allowed': $comboboxOption.isDisabled,
    }"
    ...>
    <span>Laravel</span>
    <span x-show="$comboboxOption.isSelected">&check;</span>
</li>
```

## Disabling an option

You can disable an option by adding the disabled attribute to a x-combobox:option element. This will make this option un-selectable and will be skipped when navigating through options using the arrow-keys.

```html
<li x-combobox:option disabled>
    <span>Laravel</span>
</li>
```

## Manually showing/hiding the combobox

The Combobox component manages its open state internally and automatically shows/hides the options based on that state.

If you would prefer to keep the x-combobox:options element open permanently, you may add the static attribute on the x-combobox:options element.

You can also access the internally managed open state using $combobox.isOpen.

```html
<div x-data="{ selected: null, ... }">
    <div x-combobox x-model="selected">
        <input type="text" x-combobox:input>
        <button x-combobox:button>...</button>

        <div x-show="$combobox.isOpen">
            <ul x-combobox:options static>
                ...
            </ul>
        </div>
    </div>
</div>
```

## Transitions

The Combobox component works well with Alpine transitions feature. Just add x-transition to the x-combobox:options element with the appropriate origin modifier based on your styling to apply smooth open/close transitions.

```html
<div x-data="{ selected: null, ... }">
    <div x-combobox x-model="selected">
        <input type="text" x-combobox:input>
        <button x-combobox:button>...</button>

        <ul x-combobox:options x-transition.origin.top.right>
            ...
        </ul>
    </div>
</div>
```

## Selecting multiple values

By default, the Combobox component only allows a single option to be selected at a time. If you would like the user to be able to select multiple options, pass a multiple prop to the x-combobox element.

```html
<div x-data="{ selected: [], ... }">
    <div x-combobox x-model="selected" multiple>
        ...
    </div>
</div>
```

When selecting an option while multiple is enabled, the option value will be added to an array and the x-combobox:options will remain open until the esc key is pressed or the user clicks outside the Combobox.

## Binding objects as values

Traditional HTML form inputs do not support using objects as values, but the x-combobox component does.

In order for the component to work correctly, ensure that you always use the same instance of the value objects, otherwise the component may not test equality correctly.

To make it easier to work with different instances of the same object, you can use the by prop to compare the objects by a particular property instead of comparing objects by their identity:

```html
<div x-combobox x-model="framework" by="id">
    ...
</div>
```

## Allowing empty values

By default, the Combobox component does not allow the user to clear the component value after they have selected an option - even when they tab away or press the esc key.

If you would like the user to be able to "unselect" the selected option, pass a nullable prop to the x-combobox element.

```html
<div x-data="{ query: '', selected: null, ... }">
    <div x-combobox x-model="selected" nullable>
        <input type="text" x-combobox:input
               @change="query = $event.target.value"
               :display-value="person => person?.name">
        ...
    </div>
</div>
```

## Using as an HTML form input

If you are using the component inside an HTML form, you may pass a name prop to the x-combobox element and Alpine will create a hidden input that is kept in sync with the value of the Combobox.

```html
<div x-data="{ selected: null, ... }">
    <div x-combobox name="framework" x-model="selected">
        ...
    </div>
</div>
```

## Using as an uncontrolled component

If no x-model is bound to the x-combobox element, the component will manage its own state automatically. In this case, you may set a default-value attribute on the x-combobox element to specify which option should be checked when the page is initially loaded.

```html
<div x-data>
    <div x-combobox default-value="laravel">
        ...
    </div>
</div>
```

## Adding a custom label

Headless Alpine will use the x-combobox:button contents as the default label. If you would like more control over the label, you may add x-combobox:label to an element to use it as the label for the Combobox.

```html
<div x-data="{ selected: null }">
    <div x-combobox x-model="selected">
        <span x-combobox:label>Backend framework</span>

        <ul x-combobox:options>
            ...
        </ul>
    </div>
</div>
```

## Keyboard Shortcuts

| Key | Description |
|-----|-------------|
| Enter/Space | Open the Combobox when closed or select the focused option when the Combobox is open |
| Escape | Close the Combobox |
| Up/Down | Focuses the next/previous non-disabled item |
| Home/PageUp | Focuses the first non-disabled item |
| End/PageDown | Focuses the last non-disabled item |
| A-z | Allows you to filter the options |

## API Reference

### x-combobox

The main directive for the Combobox component, used to contain the behavior for the Combobox, its button, label, and options.

| Attributes | Description |
|------------|-------------|
| x-model | Used to control which option is currently selected using outside data |
| name | Used to create a hidden input with the passed name that can be used for traditional HTML form submissions |
| disabled | Used to disable the entire component and prevent opening the options panel and selecting items |
| default-value | A mixed value used to set the default selected option |
| multiple | A boolean used to allow users to select multiple options |
| nullable | A boolean used to allow users to "unselect" the currently selected option |
| hold | A boolean used to control whether the active option stays active when the mouse leaves the element |
| by | A string key or function used to set the key or comparison function the Combobox uses to compare options for the active/selected states |

### $combobox

A magic variable that exposes information about the current state of the Combobox (element containing x-combobox).

| Properties | Description |
|------------|-------------|
| value | The currently selected value |
| isOpen | A boolean used to determine whether or not the options panel is open |
| isDisabled | A boolean used to determine whether or not the entire component is disabled |
| activeOption | The currently active option value |
| activeIndex | The currently active option index |

### x-combobox:button

Used to specify the button that will open/close the x-combobox:options panel.

### x-combobox:input

Used to specify the input that will be used to search through the options.

### x-combobox:options

Used to specify the panel that contains the options. This is the element that will be opened and closed when the x-combobox:button is clicked or the x-combobox:input is typed in.

| Attributes | Description |
|------------|-------------|
| static | A boolean used to disable the internal open/closed state so you can manually show or hide the options |

### x-combobox:option

Used to specify an individual option.

| Attributes | Description |
|------------|-------------|
| value | The value of the option |
| disabled | A boolean used to disable the option |

### $comboboxOption

A magic variable that exposes information about the current state of the option (element containing x-combobox:option).

| Properties | Description |
|------------|-------------|
| isActive | A boolean used to determine whether or not an option is currently active |
| isSelected | A boolean used to determine whether or not an option is currently selected |
| isDisabled | A boolean used to determine whether or not an option is currently disabled |

### x-combobox:label

Used to specify a custom label for the Combobox.