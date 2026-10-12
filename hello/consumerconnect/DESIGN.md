---
name: ConsumerConnect
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#554242'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#887271'
  outline-variant: '#dbc0bf'
  surface-tint: '#9b4245'
  primary: '#4d0710'
  on-primary: '#ffffff'
  primary-container: '#6b1e23'
  on-primary-container: '#f08586'
  inverse-primary: '#ffb3b2'
  secondary: '#625e56'
  on-secondary: '#ffffff'
  secondary-container: '#e8e2d8'
  on-secondary-container: '#68645c'
  tertiary: '#755b00'
  on-tertiary: '#ffffff'
  tertiary-container: '#cea62c'
  on-tertiary-container: '#4f3d00'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad9'
  primary-fixed-dim: '#ffb3b2'
  on-primary-fixed: '#410008'
  on-primary-fixed-variant: '#7c2b2f'
  secondary-fixed: '#e8e2d8'
  secondary-fixed-dim: '#ccc6bc'
  on-secondary-fixed: '#1e1b15'
  on-secondary-fixed-variant: '#4a463f'
  tertiary-fixed: '#ffe08e'
  tertiary-fixed-dim: '#ecc246'
  on-tertiary-fixed: '#241a00'
  on-tertiary-fixed-variant: '#584400'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  headline-xl:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 60px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
  headline-md:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
---

## Brand & Style

The design system is engineered to project authority, accessibility, and reassurance. It serves as a bridge between official government oversight and the modern Indian consumer, balancing traditional institutional trust with contemporary digital usability.

The aesthetic follows a **Corporate / Modern** approach with **Minimalist** leanings. It avoids aggressive marketing patterns in favor of a "Citizen-First" philosophy. Key characteristics include:
- **Dignified Presence:** Heavy use of serif headings to evoke legal and historical weight.
- **Clarity of Information:** High-contrast text and structured information hierarchies.
- **Trust-Building Layouts:** Generous whitespace to reduce cognitive load during potentially stressful consumer dispute processes.
- **Subtle Ornamentation:** Use of gold accents and thin borders rather than heavy shadows or complex gradients.

## Colors

The palette is rooted in a heritage-inspired spectrum that signifies stability and officiality.

- **Primary (Deep Maroon):** Used for structural navigation, primary calls to action, and headers. It represents the strength and authority of the portal.
- **Background (Warm Cream):** Replaces clinical white to create a more approachable, "paper-like" reading experience that reduces eye strain.
- **Accent (Soft Gold):** Reserved for highlighting status, icons, and critical data points. It should be used sparingly to maintain its significance.
- **Neutral (Charcoal/Black):** For all body text and form inputs, ensuring maximum legibility and adherence to accessibility standards (WCAG AA/AAA).

## Typography

This design system utilizes a high-contrast typographic pair to separate "Editorial/Official" voice from "Functional/Instructional" voice.

- **Headings:** Use **Playfair Display** for all page titles and section headers. Its transition between thick and thin strokes provides a sense of prestige and literary tradition.
- **Body & Controls:** Use **Inter** for all functional text. It is optimized for screen legibility, particularly for complex form labels and long-form consumer rights articles.
- **Sizing Policy:** Desktop headings use fluid scaling. On mobile devices, `headline-lg` must downscale to `headline-lg-mobile` to maintain layout integrity.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop to maintain an authoritative, centered document feel, transitioning to a fluid model for mobile devices.

- **Grid:** A 12-column grid is used for desktop (1280px max-width).
- **Rhythm:** An 8px linear scale governs all padding and margins. 
- **Breakpoints:**
  - **Mobile (< 600px):** 4-column grid, 16px side margins.
  - **Tablet (600px - 1024px):** 8-column grid, 24px side margins.
  - **Desktop (> 1024px):** 12-column grid, centered content.
- **Vertical Spacing:** Use larger gaps (48px+) between major sections to emphasize the clean, uncluttered nature of the portal.

## Elevation & Depth

This design system avoids heavy shadows to maintain a clean, institutional look. Depth is conveyed through **Low-Contrast Outlines** and **Tonal Layers**.

- **Surfaces:** Primary content sits on the Warm Cream background. Secondary containers (like sidebars or info boxes) use a slightly darker tint of the background or a thin Maroon border.
- **Outlines:** Use 1px borders in Maroon (at 20% opacity) for cards and sections. 
- **Active States:** Only active interactive elements (like an open modal) should use a subtle, highly diffused shadow (Blur: 16px, Opacity: 5%, Color: Primary).

## Shapes

The shape language is **Soft** and professional. 

- **Standard Elements:** Rectilinear forms with subtle `0.25rem` corners maintain a sense of order and structure.
- **Functional Accents:** Badges, tags, and status indicators use the **Pill-shaped** (`rounded-xl`) style to differentiate them from structural containers.
- **Inputs:** Form fields should remain strictly rectangular or use the minimum `soft` radius to ensure they feel like official documents.

## Components

### Buttons
- **Primary:** Solid Deep Maroon with White text. No gradients.
- **Secondary:** Transparent background with a 1px Maroon border.
- **Tertiary/Ghost:** Maroon text with no border, used for low-priority actions.

### Cards
- Surfaces should be the base Warm Cream.
- Use a 1px border of Deep Maroon at 15% opacity. 
- No shadows in the default state; on hover, the border opacity may increase to 40%.

### Badges & Chips
- Status indicators (e.g., "Resolved", "Pending") must be pill-shaped.
- Use Soft Gold backgrounds with dark text for highlights, and Maroon backgrounds with white text for categories.

### Accordions
- Used for FAQs and legal clauses. 
- Use a simple horizontal divider (0.5px Maroon) between items. 
- The toggle icon should be a clean chevron in Soft Gold.

### Form Fields
- Labels must be in Inter (Bold) for clarity.
- Focus state is indicated by a 2px Deep Maroon bottom border or subtle halo, avoiding high-glow effects.

### Navigation Bar
- A solid Deep Maroon bar at the top with the portal logo in White/Gold.
- Links should use Inter in a semi-bold weight.