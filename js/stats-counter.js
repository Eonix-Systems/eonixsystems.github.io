document.addEventListener("DOMContentLoaded", () => {
    const statsSection = document.querySelector('.stats-section');
    if (!statsSection) return;

    const counters = document.querySelectorAll('.stat-number');
    let hasRun = false;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !hasRun) {
                hasRun = true;
                counters.forEach(counter => {
                    // Force a starting text of 0 immediately prior to counting
                    counter.innerText = '0';
                    const updateCount = () => {
                        const target = +counter.getAttribute('data-target');
                        // Custom speed control; lower target needs slower division relative to high target
                        // We normalize speed so all counters finish roughly around the same time.
                        const speed = 40; 
                        const count = +counter.innerText;
                        
                        const inc = target / speed;

                        if (count < target) {
                            counter.innerText = Math.ceil(count + inc);
                            setTimeout(updateCount, 40);
                        } else {
                            counter.innerText = target;
                        }
                    };
                    updateCount();
                });
            }
        });
    }, { threshold: 0.3 });

    observer.observe(statsSection);
});
