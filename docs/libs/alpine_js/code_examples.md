# Dropdown


<div class="flex justify-center">
    <div
        x-data="{
            open: false,
            toggle() {
                if (this.open) {
                    return this.close()
                }

                this.$refs.button.focus()

                this.open = true
            },
            close(focusAfter) {
                if (! this.open) return

                this.open = false

                focusAfter && focusAfter.focus()
            }
        }"
        x-on:keydown.escape.prevent.stop="close($refs.button)"
        x-on:focusin.window="! $refs.panel.contains($event.target) && close()"
        x-id="['dropdown-button']"
        class="relative"
    >
        <!-- Button -->
        <button
            x-ref="button"
            x-on:click="toggle()"
            :aria-expanded="open"
            :aria-controls="$id('dropdown-button')"
            type="button"
            class="relative flex items-center whitespace-nowrap justify-center gap-2 py-2 rounded-lg shadow-sm bg-white hover:bg-gray-50 text-gray-800 border border-gray-200 hover:border-gray-200 px-4"
        >
            <span>Options</span>

            <!-- Heroicon: micro chevron-down -->
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="size-4">
                <path fill-rule="evenodd" d="M4.22 6.22a.75.75 0 0 1 1.06 0L8 8.94l2.72-2.72a.75.75 0 1 1 1.06 1.06l-3.25 3.25a.75.75 0 0 1-1.06 0L4.22 7.28a.75.75 0 0 1 0-1.06Z" clip-rule="evenodd" />
            </svg>
        </button>

        <!-- Panel -->
        <div
            x-ref="panel"
            x-show="open"
            x-transition.origin.top.left
            x-on:click.outside="close($refs.button)"
            :id="$id('dropdown-button')"
            x-cloak
            class="absolute left-0 min-w-48 rounded-lg shadow-sm mt-2 z-10 origin-top-left bg-white p-1.5 outline-none border border-gray-200"
        >
            <a href="#new" class="px-2 lg:py-1.5 py-2 w-full flex items-center rounded-md transition-colors text-left text-gray-800 hover:bg-gray-50 focus-visible:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed">
                New Task
            </a>

            <a href="#edit" class="px-2 lg:py-1.5 py-2 w-full flex items-center rounded-md transition-colors text-left text-gray-800 hover:bg-gray-50 focus-visible:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed">
                Edit Task
            </a>

            <a href="#delete" class="px-2 lg:py-1.5 py-2 w-full flex items-center rounded-md transition-colors text-left text-gray-800 hover:bg-red-50 hover:text-red-600 focus-visible:bg-red-50 focus-visible:text-red-600 disabled:opacity-50 disabled:cursor-not-allowed">
                Delete Task
            </a>
        </div>
    </div>
</div>

# Modal


<div x-data="{ open: false }" class="flex justify-center">
    <!-- Trigger -->
    <span x-on:click="open = true">
        <button type="button" class="relative flex items-center justify-center gap-2 whitespace-nowrap rounded-lg border border-gray-200 bg-white px-4 py-2 text-gray-800 shadow-sm hover:border-gray-200 hover:bg-gray-50">
            Open modal
        </button>
    </span>

    <!-- Modal -->
    <div
        x-show="open"
        style="display: none"
        x-on:keydown.escape.prevent.stop="open = false"
        role="dialog"
        aria-modal="true"
        x-id="['modal-title']"
        :aria-labelledby="$id('modal-title')"
        class="fixed inset-0 z-10 overflow-y-auto"
    >
        <!-- Overlay -->
        <div x-show="open" x-transition.opacity class="fixed inset-0 bg-black/25"></div>

        <!-- Panel -->
        <div
            x-show="open" x-transition
            x-on:click="open = false"
            class="relative flex min-h-screen items-center justify-center p-4"
        >
            <div
                x-on:click.stop
                x-trap.noscroll.inert="open"
                class="relative min-w-96 max-w-xl rounded-xl bg-white p-6 shadow-lg"
            >
                <!-- Title -->
                <h2 class="font-medium text-gray-800" :id="$id('modal-title')">Confirm</h2>

                <!-- Content -->
                <p class="mt-2 text-gray-500 max-w-xs">Are you sure you want to learn how to create an awesome modal?</p>

                <!-- Buttons -->
                <div class="mt-6 flex justify-end space-x-2">
                    <button type="button" x-on:click="open = false" class="relative flex items-center justify-center gap-2 whitespace-nowrap rounded-lg border border-transparent bg-transparent px-4 py-2 text-gray-800 hover:bg-gray-800/10">
                        Cancel
                    </button>

                    <button type="button" x-on:click="open = false" class="relative flex items-center justify-center gap-2 whitespace-nowrap rounded-lg border border-transparent bg-gray-800 px-4 py-2 text-white hover:bg-gray-900">
                        Confirm
                    </button>
                </div>
            </div>
        </div>
    </div>
</div>

# Accordion


<div x-data="{ active: 2 }" class="mx-auto min-h-[16rem] w-full max-w-3xl">
    <div x-data="{
        id: 1,
        get expanded() {
            return this.active === this.id
        },
        set expanded(value) {
            this.active = value ? this.id : null
        },
    }" role="region" class="block border-b border-gray-800/10 pb-4 pt-4 first:pt-0 last:border-b-0 last:pb-0">
        <h2>
            <button
                type="button"
                x-on:click="expanded = !expanded"
                :aria-expanded="expanded"
                class="group flex w-full items-center justify-between text-left font-medium text-gray-800"
            >
                <span class="flex-1">Question #1</span>

                <!-- Heroicons mini chevron-up -->
                <svg x-show="expanded" x-cloak class="size-5 shrink-0 text-gray-300 group-hover:text-gray-800" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M9.47 6.47a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 1 1-1.06 1.06L10 8.06l-3.72 3.72a.75.75 0 0 1-1.06-1.06l4.25-4.25Z" clip-rule="evenodd"></path>
                </svg>

                <!-- Heroicons mini chevron-down -->
                <svg x-show="!expanded" class="size-5 shrink-0 text-gray-300 group-hover:text-gray-800" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" data-slot="icon">
                    <path fill-rule="evenodd" d="M5.22 8.22a.75.75 0 0 1 1.06 0L10 11.94l3.72-3.72a.75.75 0 1 1 1.06 1.06l-4.25 4.25a.75.75 0 0 1-1.06 0L5.22 9.28a.75.75 0 0 1 0-1.06Z" clip-rule="evenodd"></path>
                </svg>
            </button>
        </h2>

        <div x-show="expanded" x-collapse>
            <div class="pt-2 text-gray-600 max-w-xl">Lorem ipsum dolor sit amet consectetur adipisicing elit. In magnam quod natus deleniti architecto eaque consequuntur ex, illo neque iste repellendus modi, quasi ipsa commodi saepe? Provident ipsa nulla earum.</div>
        </div>
    </div>

    <div x-data="{
        id: 2,
        get expanded() {
            return this.active === this.id
        },
        set expanded(value) {
            this.active = value ? this.id : null
        },
    }" role="region" class="block border-b border-gray-800/10 pb-4 pt-4 first:pt-0 last:border-b-0 last:pb-0">
        <h2>
            <button
                type="button"
                x-on:click="expanded = !expanded"
                :aria-expanded="expanded"
                class="group flex w-full items-center justify-between text-left font-medium text-gray-800"
            >
                <span class="flex-1">Question #2</span>

                <!-- Heroicons mini chevron-up -->
                <svg x-show="expanded" x-cloak class="size-5 shrink-0 text-gray-300 group-hover:text-gray-800" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M9.47 6.47a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 1 1-1.06 1.06L10 8.06l-3.72 3.72a.75.75 0 0 1-1.06-1.06l4.25-4.25Z" clip-rule="evenodd"></path>
                </svg>

                <!-- Heroicons mini chevron-down -->
                <svg x-show="!expanded" class="size-5 shrink-0 text-gray-300 group-hover:text-gray-800" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" data-slot="icon">
                    <path fill-rule="evenodd" d="M5.22 8.22a.75.75 0 0 1 1.06 0L10 11.94l3.72-3.72a.75.75 0 1 1 1.06 1.06l-4.25 4.25a.75.75 0 0 1-1.06 0L5.22 9.28a.75.75 0 0 1 0-1.06Z" clip-rule="evenodd"></path>
                </svg>
            </button>
        </h2>

        <div x-show="expanded" x-collapse>
            <div class="pt-2 text-gray-600 max-w-xl">Lorem ipsum dolor sit amet consectetur adipisicing elit. In magnam quod natus deleniti architecto eaque consequuntur ex, illo neque iste repellendus modi, quasi ipsa commodi saepe? Provident ipsa nulla earum.</div>
        </div>
    </div>
</div>

# Carousel


<script src="https://unpkg.com/smoothscroll-polyfill@0.4.4/dist/smoothscroll.js"></script>

<div
    x-data="{
        skip: 3,
        atBeginning: false,
        atEnd: false,
        next() {
            this.to((current, offset) => current + (offset * this.skip))
        },
        prev() {
            this.to((current, offset) => current - (offset * this.skip))
        },
        to(strategy) {
            let slider = this.$refs.slider
            let current = slider.scrollLeft
            let offset = slider.firstElementChild.getBoundingClientRect().width
            slider.scrollTo({ left: strategy(current, offset), behavior: 'smooth' })
        },
        focusableWhenVisible: {
            'x-intersect:enter'() {
                this.$el.removeAttribute('tabindex')
            },
            'x-intersect:leave'() {
                this.$el.setAttribute('tabindex', '-1')
            },
        },
        disableNextAndPreviousButtons: {
            'x-intersect:enter.threshold.05'() {
                let slideEls = this.$el.parentElement.children

                // If this is the first slide.
                if (slideEls[0] === this.$el) {
                    this.atBeginning = true
                // If this is the last slide.
                } else if (slideEls[slideEls.length-1] === this.$el) {
                    this.atEnd = true
                }
            },
            'x-intersect:leave.threshold.05'() {
                let slideEls = this.$el.parentElement.children

                // If this is the first slide.
                if (slideEls[0] === this.$el) {
                    this.atBeginning = false
                // If this is the last slide.
                } else if (slideEls[slideEls.length-1] === this.$el) {
                    this.atEnd = false
                }
            },
        },
    }"
    class="flex w-full flex-col"
>
    <div
        x-on:keydown.right="next"
        x-on:keydown.left="prev"
        tabindex="0"
        role="region"
        aria-labelledby="carousel-label"
        class="flex space-x-6"
    >
        <h2 id="carousel-label" class="sr-only" hidden>Carousel</h2>

        <!-- Prev Button -->
        <button
            x-on:click="prev"
            class="text-6xl"
            :aria-disabled="atBeginning"
            :tabindex="atEnd ? -1 : 0"
            :class="{ 'opacity-50 cursor-not-allowed': atBeginning }"
        >
            <span aria-hidden="true">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6 text-gray-800">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5 8.25 12l7.5-7.5" />
                </svg>
            </span>
            <span class="sr-only">Skip to previous slide page</span>
        </button>

        <span id="carousel-content-label" class="sr-only" hidden>Carousel</span>

        <ul
            x-ref="slider"
            tabindex="0"
            role="listbox"
            aria-labelledby="carousel-content-label"
            class="flex w-full snap-x snap-mandatory overflow-x-scroll"
        >
            <li x-bind="disableNextAndPreviousButtons" class="flex w-1/3 shrink-0 snap-start flex-col items-center justify-center p-2" role="option">
                <div class="rounded-lg shadow-sm mt-2 w-full overflow-hidden aspect-square bg-gray-200">
                    <img class="w-full h-full" src="https://picsum.photos/400/400?random=1" alt="placeholder image">
                </div>

                <button x-bind="focusableWhenVisible" class="p-2 text-sm text-gray-800 font-medium">1</button>
            </li>

            <li x-bind="disableNextAndPreviousButtons" class="flex w-1/3 shrink-0 snap-start flex-col items-center justify-center p-2" role="option">
                <div class="rounded-lg shadow-sm mt-2 w-full overflow-hidden aspect-square bg-gray-200">
                    <img class="w-full h-full" src="https://picsum.photos/400/400?random=2" alt="placeholder image">
                </div>

                <button x-bind="focusableWhenVisible" class="p-2 text-sm text-gray-800 font-medium">2</button>
            </li>

            <li x-bind="disableNextAndPreviousButtons" class="flex w-1/3 shrink-0 snap-start flex-col items-center justify-center p-2" role="option">
                <div class="rounded-lg shadow-sm mt-2 w-full overflow-hidden aspect-square bg-gray-200">
                    <img class="w-full h-full" src="https://picsum.photos/400/400?random=3" alt="placeholder image">
                </div>

                <button x-bind="focusableWhenVisible" class="p-2 text-sm text-gray-800 font-medium">3</button>
            </li>

            <li x-bind="disableNextAndPreviousButtons" class="flex w-1/3 shrink-0 snap-start flex-col items-center justify-center p-2" role="option">
                <div class="rounded-lg shadow-sm mt-2 w-full overflow-hidden aspect-square bg-gray-200">
                    <img class="w-full h-full" src="https://picsum.photos/400/400?random=4" alt="placeholder image">
                </div>

                <button x-bind="focusableWhenVisible" class="p-2 text-sm text-gray-800 font-medium">4</button>
            </li>

            <li x-bind="disableNextAndPreviousButtons" class="flex w-1/3 shrink-0 snap-start flex-col items-center justify-center p-2" role="option">
                <div class="rounded-lg shadow-sm mt-2 w-full overflow-hidden aspect-square bg-gray-200">
                    <img class="w-full h-full" src="https://picsum.photos/400/400?random=5" alt="placeholder image">
                </div>

                <button x-bind="focusableWhenVisible" class="p-2 text-sm text-gray-800 font-medium">5</button>
            </li>

            <li x-bind="disableNextAndPreviousButtons" class="flex w-1/3 shrink-0 snap-start flex-col items-center justify-center p-2" role="option">
                <div class="rounded-lg shadow-sm mt-2 w-full overflow-hidden aspect-square bg-gray-200">
                    <img class="w-full h-full" src="https://picsum.photos/400/400?random=6" alt="placeholder image">
                </div>

                <button x-bind="focusableWhenVisible" class="p-2 text-sm text-gray-800 font-medium">6</button>
            </li>
        </ul>

        <!-- Next Button -->
        <button
            x-on:click="next"
            class="text-6xl"
            :aria-disabled="atEnd"
            :tabindex="atEnd ? -1 : 0"
            :class="{ 'opacity-50 cursor-not-allowed': atEnd }"
        >
            <span aria-hidden="true">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6 text-gray-800">
                    <path stroke-linecap="round" stroke-linejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5" />
                </svg>
            </span>
            <span class="sr-only">Skip to next slide page</span>
        </button>
    </div>
</div>

# Tabs


<!-- Tabs -->
<div
    x-data="{
        selectedId: null,
        init() {
            // Set the first available tab on the page on page load.
            this.$nextTick(() => this.select(this.$id('tab', 1)))
        },
        select(id) {
            this.selectedId = id
        },
        isSelected(id) {
            return this.selectedId === id
        },
        whichChild(el, parent) {
            return Array.from(parent.children).indexOf(el) + 1
        }
    }"
    x-id="['tab']"
    class="mx-auto max-w-3xl"
>
    <!-- Tab List -->
    <ul
        x-ref="tablist"
        @keydown.right.prevent.stop="$focus.wrap().next()"
        @keydown.home.prevent.stop="$focus.first()"
        @keydown.page-up.prevent.stop="$focus.first()"
        @keydown.left.prevent.stop="$focus.wrap().prev()"
        @keydown.end.prevent.stop="$focus.last()"
        @keydown.page-down.prevent.stop="$focus.last()"
        role="tablist"
        class="-mb-px flex items-stretch overflow-x-auto"
    >
        <!-- Tab -->
        <li>
            <button
                :id="$id('tab', whichChild($el.parentElement, $refs.tablist))"
                @click="select($el.id)"
                @mousedown.prevent
                @focus="select($el.id)"
                type="button"
                :tabindex="isSelected($el.id) ? 0 : -1"
                :aria-selected="isSelected($el.id)"
                :class="isSelected($el.id) ? 'border-gray-200 bg-white' : 'border-transparent'"
                class="inline-flex rounded-t-lg border-t border-l border-r px-5 py-2.5"
                role="tab"
            >Tab 1</button>
        </li>

        <li>
            <button
                :id="$id('tab', whichChild($el.parentElement, $refs.tablist))"
                @click="select($el.id)"
                @mousedown.prevent
                @focus="select($el.id)"
                type="button"
                :tabindex="isSelected($el.id) ? 0 : -1"
                :aria-selected="isSelected($el.id)"
                :class="isSelected($el.id) ? 'border-gray-200 bg-white' : 'border-transparent'"
                class="inline-flex rounded-t-lg border-t border-l border-r px-5 py-2.5"
                role="tab"
            >Tab 2</button>
        </li>
    </ul>

    <!-- Panels -->
    <div role="tabpanels" class="rounded-b-lg rounded-tr-lg border border-gray-200 bg-white">
        <!-- Panel -->
        <section
            x-show="isSelected($id('tab', whichChild($el, $el.parentElement)))"
            :aria-labelledby="$id('tab', whichChild($el, $el.parentElement))"
            role="tabpanel"
            class="p-8"
        >
            <h2 class="text-xl font-bold">Tab 1 Content</h2>
            <p class="mt-2 text-gray-500">Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio, quo sequi error quibusdam quas temporibus animi sapiente eligendi! Deleniti minima velit recusandae iure.</p>
            <button class="mt-5 rounded-lg border border-gray-200 px-4 py-2 text-sm text-gray-800">Something focusable</button>
        </section>

        <section
            x-show="isSelected($id('tab', whichChild($el, $el.parentElement)))"
            :aria-labelledby="$id('tab', whichChild($el, $el.parentElement))"
            role="tabpanel"
            class="p-8"
        >
            <h2 class="text-xl font-bold">Tab 2 Content</h2>
            <p class="mt-2 text-gray-500">Fugiat odit alias, eaque optio quas nobis minima reiciendis voluptate dolorem nisi facere debitis ea laboriosam vitae omnis ut voluptatum eos. Fugiat?</p>
            <button class="mt-5 rounded-lg border border-gray-200 px-4 py-2 text-sm text-gray-800">Something else focusable</button>
        </section>
    </div>
</div>

# Notifications

<div
    x-data="{
        notifications: [],
        add(e) {
            this.notifications.push({
                id: e.timeStamp,
                type: e.detail.type,
                content: e.detail.content,
            })
        },
        remove(notification) {
            this.notifications = this.notifications.filter(i => i.id !== notification.id)
        },
    }"
    @notify.window="add($event)"
    class="fixed bottom-0 right-0 flex w-full max-w-sm flex-col space-y-4 pr-4 pb-4 sm:justify-start z-10"
    role="status"
    aria-live="polite"
>
    <!-- Notification -->
    <template x-for="notification in notifications" :key="notification.id">
        <div
            x-data="{
                show: false,
                init() {
                    this.$nextTick(() => this.show = true)

                    setTimeout(() => this.transitionOut(), 2000)
                },
                transitionOut() {
                    this.show = false

                    setTimeout(() => this.remove(this.notification), 500)
                },
            }"
            x-show="show"
            x-transition.duration.500ms
            class="pointer-events-auto relative w-full max-w-sm rounded-lg border border-gray-200 bg-white p-2 shadow-lg"
        >
            <div class="flex items-start gap-4">
                <div class="flex-1 py-1.5 pl-2.5 flex gap-2">
                    <!-- Icons -->
                    <div x-show="notification.type === 'info'" class="flex-shrink-0">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="mt-0.5 size-4 text-gray-600">
                            <path fill-rule="evenodd" d="M15 8A7 7 0 1 1 1 8a7 7 0 0 1 14 0ZM9 5a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM6.75 8a.75.75 0 0 0 0 1.5h.75v1.75a.75.75 0 0 0 1.5 0v-2.5A.75.75 0 0 0 8.25 8h-1.5Z" clip-rule="evenodd" />
                        </svg>
                        <span class="sr-only">Information:</span>
                    </div>

                    <div x-show="notification.type === 'success'" class="flex-shrink-0">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="mt-0.5 size-4 text-green-600">
                            <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14Zm3.844-8.791a.75.75 0 0 0-1.188-.918l-3.7 4.79-1.649-1.833a.75.75 0 1 0-1.114 1.004l2.25 2.5a.75.75 0 0 0 1.15-.043l4.25-5.5Z" clip-rule="evenodd"></path>
                        </svg>
                        <span class="sr-only">Success:</span>
                    </div>

                    <div x-show="notification.type === 'error'" class="flex-shrink-0">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="mt-0.5 size-4 text-red-600">
                            <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14ZM8 4a.75.75 0 0 1 .75.75v3a.75.75 0 0 1-1.5 0v-3A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z" clip-rule="evenodd"></path>
                        </svg>
                        <span class="sr-only">Error:</span>
                    </div>

                    <!-- Text -->
                    <div class="flex flex-col gap-y-2">
                        <p x-text="notification.type" class="capitalize font-medium text-sm text-gray-800"></p>

                        <div class="text-sm text-gray-600" x-text="notification.content"></div>
                    </div>
                </div>
                <!-- Remove button -->
                <div class="flex items-center">
                    <button @click="transitionOut()" type="button" class="inline-flex items-center font-medium justify-center p-1.5 rounded-md hover:bg-gray-800/5 text-gray-400 hover:text-gray-800">
                        <svg aria-hidden class="size-5" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                        </svg>
                        <span class="sr-only">Close notification</span>
                    </button>
                </div>
            </div>
        </div>
    </template>
</div>

<!-- Examples of how to dispatch the `notify` event with variable text and type -->
<form
    x-data="{
        content: 'Something happened!',
        type: 'info',
    }"
    class="max-w-sm w-full"
    x-on:submit.prevent="$dispatch('notify', { content, type })"
>
    <div>
        <label for="message" class="text-sm font-medium select-none text-gray-800">Message</label>

        <input type="text" id="message" x-model="content" class="mt-3 w-full rounded-lg border border-gray-200 bg-white px-3 py-2 shadow-sm" placeholder="">
    </div>

    <div class="mt-6">
        <label for="type" class="text-sm font-medium select-none text-gray-800">
            Type
        </label>

        <select id="type" x-model="type" type="text" class="mt-3 w-full rounded-lg border border-gray-200 bg-white px-3 py-2 shadow-sm">
            <option value="info">Info</option>
            <option value="success">Success</option>
            <option value="error">Error</option>
        </select>
    </div>

    <div class="mt-8">
        <button class="relative flex items-center justify-center gap-2 whitespace-nowrap rounded-lg border border-gray-200 bg-white px-4 py-2 text-gray-800 shadow-sm hover:border-gray-200 hover:bg-gray-50">
            Dispatch notification
        </button>
    </div>
</form>

# Radio Group


<!-- Radio Group -->
<div
    x-data="{
        value: 'laravel',
        select(option) { this.value = option },
        isSelected(option) { return this.value === option },
        hasRovingTabindex(option, el) {
            // If this is the first option element and no option has been selected, make it focusable.
            if (this.value === null && Array.from(el.parentElement.children).indexOf(el) === 0) return true

            return this.isSelected(option)
        },
        selectNext(e) {
            let el = e.target
            let siblings = Array.from(el.parentElement.children)
            let index = siblings.indexOf(el)
            let next = siblings[index === siblings.length - 1 ? 0 : index + 1]

            next.click(); next.focus();
        },
        selectPrevious(e) {
            let el = e.target
            let siblings = Array.from(el.parentElement.children)
            let index = siblings.indexOf(el)
            let previous = siblings[index === 0 ? siblings.length - 1 : index - 1]

            previous.click(); previous.focus();
        },
    }"
    @keydown.down.stop.prevent="selectNext"
    @keydown.right.stop.prevent="selectNext"
    @keydown.up.stop.prevent="selectPrevious"
    @keydown.left.stop.prevent="selectPrevious"
    role="radiogroup"
    :aria-labelledby="$id('radio-group-label')"
    x-id="['radio-group-label']"
    class="max-w-2xl w-full"
>
    <!-- Radio Group Label -->
    <label :id="$id('radio-group-label')" role="none" class="sr-only">Backend framework: <span x-text="value"></span></label>

    <div class="flex gap-3 max-sm:flex-col">
        <!-- Option -->
        <div
            x-data="{ option: 'laravel' }"
            @click="select(option)"
            @keydown.enter.stop.prevent="select(option)"
            @keydown.space.stop.prevent="select(option)"
            :aria-checked="isSelected(option)"
            :tabindex="hasRovingTabindex(option, $el) ? 0 : -1"
            :aria-labelledby="$id('radio-option-label')"
            :aria-describedby="$id('radio-option-description')"
            x-id="['radio-option-label', 'radio-option-description']"
            role="radio"
            :class="isSelected(option) ? 'bg-gray-50 border-gray-600' : 'bg-white border-gray-800/15'"
            class="flex flex-1 cursor-pointer justify-between gap-3 rounded-lg border p-4 shadow-sm hover:bg-gray-50"
        >
            <div class="flex flex-1 gap-2">
                <div>
                    <!-- Primary Label -->
                    <p :id="$id('radio-option-label')" class="font-medium text-gray-800">Laravel</p>

                    <!-- Secondary Information -->
                    <div :id="$id('radio-option-description')" class="mt-2 text-sm text-gray-500">
                        A PHP framework built by Taylor Otwell
                    </div>
                </div>
            </div>

            <!-- Checked Indicator -->
            <div
                :class="isSelected(option) ? 'ring-gray-800 bg-gray-800 hover:bg-gray-800 focus:bg-gray-800' : 'ring-gray-300 bg-white'"
                class="flex size-[14px] shrink-0 items-center justify-center rounded-full text-gray-700 shadow-none ring-1 ring-offset-2"
                aria-hidden="true"
            ></div>
        </div>

        <div
            x-data="{ option: 'rails' }"
            @click="select(option)"
            @keydown.enter.stop.prevent="select(option)"
            @keydown.space.stop.prevent="select(option)"
            :aria-checked="isSelected(option)"
            :tabindex="hasRovingTabindex(option, $el) ? 0 : -1"
            :aria-labelledby="$id('radio-option-label')"
            :aria-describedby="$id('radio-option-description')"
            x-id="['radio-option-label', 'radio-option-description']"
            role="radio"
            :class="isSelected(option) ? 'bg-gray-50 border-gray-600' : 'bg-white border-gray-800/15'"
            class="flex flex-1 cursor-pointer justify-between gap-3 rounded-lg border p-4 shadow-sm hover:bg-gray-50"
        >
            <div class="flex flex-1 gap-2">
                <div>
                    <!-- Primary Label -->
                    <p :id="$id('radio-option-label')" class="font-medium text-gray-800">Rails</p>

                    <!-- Secondary Information -->
                    <div :id="$id('radio-option-description')" class="mt-2 text-sm text-gray-500">
                        A Ruby framework built by DHH
                    </div>
                </div>
            </div>

            <!-- Checked Indicator -->
            <div
                :class="isSelected(option) ? 'ring-gray-800 bg-gray-800 hover:bg-gray-800 focus:bg-gray-800' : 'ring-gray-300 bg-white'"
                class="flex size-[14px] shrink-0 items-center justify-center rounded-full text-gray-700 shadow-none ring-1 ring-offset-2"
                aria-hidden="true"
            ></div>
        </div>

        <div
            x-data="{ option: 'phoenix' }"
            @click="select(option)"
            @keydown.enter.stop.prevent="select(option)"
            @keydown.space.stop.prevent="select(option)"
            :aria-checked="isSelected(option)"
            :tabindex="hasRovingTabindex(option, $el) ? 0 : -1"
            :aria-labelledby="$id('radio-option-label')"
            :aria-describedby="$id('radio-option-description')"
            x-id="['radio-option-label', 'radio-option-description']"
            role="radio"
            :class="isSelected(option) ? 'bg-gray-50 border-gray-600' : 'bg-white border-gray-800/15'"
            class="flex flex-1 cursor-pointer justify-between gap-3 rounded-lg border p-4 shadow-sm hover:bg-gray-50"
        >
            <div class="flex flex-1 gap-2">
                <div>
                    <!-- Primary Label -->
                    <p :id="$id('radio-option-label')" class="font-medium text-gray-800">Phoenix</p>

                    <!-- Secondary Information -->
                    <div :id="$id('radio-option-description')" class="mt-2 text-sm text-gray-500">
                        An Elixir framework built by Chris McCord
                    </div>
                </div>
            </div>

            <!-- Checked Indicator -->
            <div
                :class="isSelected(option) ? 'ring-gray-800 bg-gray-800 hover:bg-gray-800 focus:bg-gray-800' : 'ring-gray-300 bg-white'"
                class="flex size-[14px] shrink-0 items-center justify-center rounded-full text-gray-700 shadow-none ring-1 ring-offset-2"
                aria-hidden="true"
            ></div>
        </div>
    </div>
</div>

# Toogle


<!-- Toggle -->
<div
    x-data="{ value: false }"
    class="flex min-w-0 gap-4 items-center"
    x-id="['toggle-label']"
>
    <input type="hidden" name="sendNotifications" :value="value">

    <!-- Label -->
    <label
        @click="$refs.toggle.click(); $refs.toggle.focus()"
        :id="$id('toggle-label')"
        class="font-medium text-gray-800 select-none"
    >
        Send notifications
    </label>

    <!-- Button -->
    <button
        x-ref="toggle"
        @click="value = ! value"
        type="button"
        role="switch"
        :aria-checked="value"
        :aria-labelledby="$id('toggle-label')"
        :class="value ? 'bg-gray-800' : 'bg-gray-800/20'"
        class="relative inline-flex h-5 w-8 items-center rounded-full outline-offset-2 transition"
    >
        <span
            :class="value ? 'translate-x-[15px]' : 'translate-x-[3px]'"
            class="bg-white size-3.5 rounded-full transition shadow-md"
            aria-hidden="true"
        ></span>
    </button>
</div>

# Tooltip


<!-- Tippy.js -->
<!-- https://atomiks.github.io/tippyjs/v6 -->
<script src="https://unpkg.com/@popperjs/core@2"></script>
<script src="https://unpkg.com/tippy.js@6"></script>

<!-- Usage -->
<div class="flex items-center justify-center gap-2">
    <button
        x-data
        x-tooltip="I am a tooltip!"
        type="button"
        class="relative flex items-center justify-center gap-2 whitespace-nowrap rounded-lg border border-gray-200 bg-white px-4 py-2 text-gray-800 shadow-sm hover:border-gray-200 hover:bg-gray-50"
    >
        Hover over me
    </button>

    <button
        x-data
        @click="$tooltip('I am a tooltip!')"
        type="button"
        class="relative flex items-center justify-center gap-2 whitespace-nowrap rounded-lg border border-gray-200 bg-white px-4 py-2 text-gray-800 shadow-sm hover:border-gray-200 hover:bg-gray-50"
    >
        Click me
    </button>
</div>

<!-- Source -->
<script>
    document.addEventListener('alpine:init', () => {
        // Magic: $tooltip
        Alpine.magic('tooltip', el => message => {
            let instance = tippy(el, { content: message, trigger: 'manual' })

            instance.show()

            setTimeout(() => {
                instance.hide()

                setTimeout(() => instance.destroy(), 150)
            }, 2000)
        })

        // Directive: x-tooltip
        Alpine.directive('tooltip', (el, { expression }) => {
            tippy(el, { content: expression })
        })
    })
</script>