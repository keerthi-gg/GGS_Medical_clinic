document.addEventListener('error', (event) => {
  const image = event.target;
  if (!(image instanceof HTMLImageElement) || !image.matches('.hero-image, .about-image')) {
    return;
  }

  const fallback = image.parentElement?.querySelector('.image-fallback');
  if (fallback) {
    fallback.hidden = false;
  }
  image.hidden = true;
}, true);

document.addEventListener('DOMContentLoaded', () => {
  const appointmentDialog = document.querySelector('#appointment-dialog');
  const appointmentTriggers = document.querySelectorAll('[data-open-appointment]');
  const closeButton = document.querySelector('[data-close-appointment]');

  for (const trigger of appointmentTriggers) {
    trigger.addEventListener('click', () => {
      if (appointmentDialog && !appointmentDialog.open) {
        appointmentDialog.showModal();
      }
    });
  }

  closeButton?.addEventListener('click', () => appointmentDialog?.close());

  appointmentDialog?.addEventListener('keydown', (event) => {
    if (event.key !== 'Tab') {
      return;
    }

    const focusable = [...appointmentDialog.querySelectorAll(
      'a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])',
    )].filter((element) => element.getClientRects().length > 0);
    const first = focusable[0];
    const last = focusable[focusable.length - 1];

    if (!first || !last) {
      event.preventDefault();
      appointmentDialog.focus();
    } else if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  });

  for (const copyButton of document.querySelectorAll('[data-copy-phone]')) {
    copyButton.addEventListener('click', async () => {
      const row = copyButton.closest('.phone-row');
      const status = row?.querySelector('.copy-status');
      const phoneNumber = row?.querySelector('[data-phone-number]');
      const phoneValue = copyButton.dataset.copyPhone;

      if (!phoneValue || !status || !phoneNumber) {
        return;
      }

      try {
        if (!window.isSecureContext || !navigator.clipboard?.writeText) {
          throw new Error('Clipboard access is unavailable in this context.');
        }

        await navigator.clipboard.writeText(phoneValue);
        status.textContent = `Copied ${phoneValue}`;
      } catch {
        const selection = window.getSelection();
        const range = document.createRange();
        range.selectNodeContents(phoneNumber);
        selection?.removeAllRanges();
        selection?.addRange(range);
        status.textContent = `Copy unavailable. ${phoneValue} is selected; copy it manually.`;
      }
    });
  }
});
