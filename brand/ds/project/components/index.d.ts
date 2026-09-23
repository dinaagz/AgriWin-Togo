/**
 * AgriWin Togo — types de la bibliothèque de composants.
 * Documentation seulement : le bundle est du JavaScript classique qui pose
 * `window.AgriWin`. Chaque fabrique renvoie un élément du DOM.
 */

export type IconName =
  | "leaf" | "school" | "users" | "shield" | "target" | "arrow"
  | "phone" | "mail" | "pin" | "calendar" | "check" | "search";

export type ButtonVariant =
  | "primary"        // or gold-500, action de conversion
  | "green"          // vert plein green-700
  | "outline"        // contour blanc, sur aplat vert uniquement
  | "outline-green"  // contour green-700, sur fond clair
  | "call"           // fond blanc, contour green-700
  | "whatsapp";      // vert de service WhatsApp

export interface ButtonProps {
  label: string;
  variant?: ButtonVariant;
  size?: "md" | "sm";
  icon?: IconName;
  href?: string;
  block?: boolean;
  disabled?: boolean;
  type?: "button" | "submit" | "reset";
  onClick?: (event: MouseEvent) => void;
}

export interface EyebrowProps { label: string; icon?: IconName; onDark?: boolean }

export interface SectionHeadProps {
  title: string;
  /** Un à trois mots, rendus en Playfair Display italique gold-700. */
  accent?: string;
  eyebrow?: string;
  lead?: string;
  center?: boolean;
  onDark?: boolean;
}

export interface CardProps {
  media?: string;
  mediaAlt?: string;
  badge?: string;
  tag?: string;
  title?: string;
  text?: string;
  children?: HTMLElement[];
  className?: string;
  /** Charge l'image en `eager` plutôt qu'en `lazy` (défaut). À réserver aux
   *  cartes visibles d'entrée : première ligne d'un catalogue, carte de hero. */
  eagerMedia?: boolean;
}

export interface ServiceCardProps {
  title: string;
  text: string;
  icon?: IconName;
  linkLabel?: string;
  href?: string;
}

export interface ValueCardProps { title: string; text: string; icon?: IconName }

export interface ProductCardProps {
  title: string;
  text?: string;
  media?: string;
  tag?: string;
  /** Francs CFA, séparateur de milliers en espace fine : « 3 500 F ». */
  price?: string;
  unit?: string;
  badge?: string;
  primaryLabel?: string;
  secondaryLabel?: string;
  /** Charge l'image en `eager` plutôt qu'en `lazy` (défaut). */
  eagerMedia?: boolean;
}

export interface StatBandProps { items: Array<{ value: string; label: string }> }

export interface CtaBandProps { title: string; text?: string; actions?: ButtonProps[] }

export interface FieldProps {
  label: string;
  /** Obligatoire : lie le libellé au contrôle. */
  id: string;
  as?: "input" | "textarea" | "select";
  type?: string;
  options?: string[];
  placeholder?: string;
  value?: string;
  note?: string;
  /** Remplace `note` quand il est présent. */
  error?: string;
  required?: boolean;
  disabled?: boolean;
  rows?: number;
}

export interface FilterChipProps {
  label: string;
  active?: boolean;
  onToggle?: (active: boolean) => void;
}

export interface ContactCardProps {
  title?: string;
  lines: Array<{ icon?: IconName; label: string; value: string }>;
}

export interface StepListProps { steps: Array<{ title: string; text: string }> }

export interface BrandProps { logo?: string; onDark?: boolean }

export declare function Icon(name: IconName, size?: number): SVGElement;
export declare function Button(props: ButtonProps): HTMLElement;
export declare function Eyebrow(props: EyebrowProps): HTMLElement;
export declare function SectionHead(props: SectionHeadProps): HTMLElement;
export declare function Card(props: CardProps): HTMLElement;
export declare function ServiceCard(props: ServiceCardProps): HTMLElement;
export declare function ValueCard(props: ValueCardProps): HTMLElement;
export declare function ProductCard(props: ProductCardProps): HTMLElement;
export declare function StatBand(props: StatBandProps): HTMLElement;
export declare function CtaBand(props: CtaBandProps): HTMLElement;
export declare function Field(props: FieldProps): HTMLElement;
export declare function FilterChip(props: FilterChipProps): HTMLElement;
export declare function ContactCard(props: ContactCardProps): HTMLElement;
export declare function StepList(props: StepListProps): HTMLElement;
export declare function Brand(props: BrandProps): HTMLElement;
